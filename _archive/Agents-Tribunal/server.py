from pathlib import Path
import io
import os

from mcp.server.fastmcp import FastMCP, Image
from PIL import Image as PILImage
import nbformat as nbf

# Tentar importar PyMuPDF (não requer Poppler)
try:
    import fitz  # PyMuPDF
    HAS_PYMUPDF = True
except ImportError:
    HAS_PYMUPDF = False

# Tentar importar pdf2image (requer Poppler) como fallback
try:
    from pdf2image import convert_from_path
    HAS_PDF2IMAGE = True
except ImportError:
    HAS_PDF2IMAGE = False


"""
Servidor MCP para processamento de slides biomédicos em PDF
e geração de notebooks Jupyter com suporte a um "Tribunal" de análise.

Ferramentas expostas:
- inspect_pdf_metadata(pdf_path: str) -> str
- process_slide_for_vision(pdf_path: str, page_number: int) -> Image
- append_to_notebook(notebook_path: str, slide_number: int,
                     analysis_text: str, biomedical_context: str,
                     relevant_links: str) -> str
"""


mcp = FastMCP("Biomedical-Slide-Processor")

# Diretório para guardar as imagens em alta resolução
CACHE_DIR = Path("notebook_images")
CACHE_DIR.mkdir(exist_ok=True)


@mcp.tool()
def inspect_pdf_metadata(pdf_path: str) -> str:
    """
    Verifica se o PDF é legível e retorna informação básica.
    Use esta ferramenta antes de iniciar a análise de slides.
    """
    if not os.path.exists(pdf_path):
        return f"Erro: ficheiro não encontrado em '{pdf_path}'."

    try:
        if HAS_PYMUPDF:
            # Usar PyMuPDF (não requer Poppler)
            doc = fitz.open(pdf_path)
            page_count = len(doc)
            doc.close()
            return f"PDF '{pdf_path}' é válido. Total de páginas: {page_count}."
        elif HAS_PDF2IMAGE:
            # Fallback para pdf2image (requer Poppler)
            _ = convert_from_path(pdf_path, first_page=1, last_page=1)
            return f"PDF '{pdf_path}' é válido e pode ser renderizado."
        else:
            return "Erro: Nenhuma biblioteca PDF disponível. Instala PyMuPDF: pip install PyMuPDF"
    except Exception as e:
        return (
            f"Falha ao ler o PDF. Erro técnico: {e}. "
            "Sugestão: Instala PyMuPDF (pip install PyMuPDF) que não requer Poppler."
        )


@mcp.tool()
def process_slide_for_vision(pdf_path: str, page_number: int) -> Image:
    """
    Renderiza uma página específica (1‑based) de um PDF como imagem.

    - Guarda PNG em alta resolução em 'notebook_images/slide_{page}.png'
    - Devolve uma versão reduzida (JPEG) para análise visual pelo modelo.
    """
    if not os.path.exists(pdf_path):
        raise RuntimeError(f"Ficheiro PDF não encontrado em '{pdf_path}'.")

    if page_number < 1:
        raise RuntimeError("page_number deve ser >= 1 (index 1‑based).")

    try:
        img: PILImage.Image = None

        if HAS_PYMUPDF:
            # Usar PyMuPDF (método preferido - não requer Poppler)
            doc = fitz.open(pdf_path)
            if page_number > len(doc):
                doc.close()
                raise RuntimeError(f"Página {page_number} fora do intervalo. PDF tem {len(doc)} páginas.")
            
            page = doc[page_number - 1]  # PyMuPDF usa índice 0-based
            # Renderizar em alta resolução (2x para melhor qualidade)
            mat = fitz.Matrix(2.0, 2.0)  # 2x zoom = maior resolução
            pix = page.get_pixmap(matrix=mat)
            img_data = pix.tobytes("png")
            img = PILImage.open(io.BytesIO(img_data))
            doc.close()

        elif HAS_PDF2IMAGE:
            # Fallback para pdf2image (requer Poppler)
            images = convert_from_path(
                pdf_path,
                first_page=page_number,
                last_page=page_number,
            )
            if not images:
                raise RuntimeError("Número de página fora do intervalo do PDF.")
            img = images[0]
        else:
            raise RuntimeError(
                "Nenhuma biblioteca PDF disponível. "
                "Instala PyMuPDF: pip install PyMuPDF"
            )

        # 1) Guardar PNG de alta resolução para o notebook
        image_filename = f"slide_{page_number}.png"
        local_path = CACHE_DIR / image_filename
        img.save(local_path, "PNG")

        # 2) Criar miniatura para envio ao modelo (eficiência de contexto)
        img_for_model = img.copy()
        img_for_model.thumbnail((1024, 1024))

        buffered = io.BytesIO()
        img_for_model.save(buffered, format="JPEG", quality=85)
        img_bytes = buffered.getvalue()

        return Image(data=img_bytes, format="jpeg")

    except Exception as e:
        raise RuntimeError(f"Falha ao processar slide {page_number}: {e}")


@mcp.tool()
def append_to_notebook(
    notebook_path: str,
    slide_number: int,
    analysis_text: str,
    biomedical_context: str,
    relevant_links: str,
    external_images: str = "",
    python_code: str = "",
) -> str:
    """
    Adiciona (ou cria) um notebook Jupyter com uma secção para um slide.

    - notebook_path: caminho do .ipynb a criar/atualizar
    - slide_number: número do slide analisado
    - analysis_text: descrição/explicação do slide (Observer + síntese)
    - biomedical_context: interpretação clínica/engenharia (Tribunal)
    - relevant_links: referências (PubMed, guidelines, etc.)
    - external_images: markdown com imagens externas (PubMed, documentos oficiais, etc.) - opcional
    - python_code: código Python executável para simulações/exercícios - opcional
    """
    nb_path = Path(notebook_path)

    if nb_path.exists():
        nb = nbf.read(nb_path, as_version=4)
    else:
        nb = nbf.v4.new_notebook()
        nb.cells.append(
            nbf.v4.new_markdown_cell(
                "# Apontamentos Biomédicos - Radioterapia\n"
                "Gerado automaticamente via servidor MCP e Tribunal de Agentes.\n"
                "\n"
                "Este notebook contém análises detalhadas, explicações profundas, "
                "exercícios resolvidos e código Python executável."
            )
        )

    # Caminho relativo da imagem a partir do notebook
    rel_image_path = f"notebook_images/slide_{slide_number}.png"

    # Incluir imagens externas se fornecidas
    external_section = ""
    if external_images.strip():
        external_section = f"\n### Imagens e Documentos Oficiais\n\n{external_images}\n"

    md_content = f"""
## Slide {slide_number}

![Slide {slide_number}]({rel_image_path})

### Análise Visual (Observer)
{analysis_text}

### Contexto Biomédico (Tribunal: Clínico + Engenheiro)
{biomedical_context}
{external_section}
---

**Literatura e Recursos Relevantes**

{relevant_links}
"""

    nb.cells.append(nbf.v4.new_markdown_cell(md_content.strip() + "\n"))
    
    # Adicionar código Python se fornecido
    if python_code.strip():
        nb.cells.append(nbf.v4.new_code_cell(python_code))
    
    nbf.write(nb, nb_path)

    return (
        f"Análise do slide {slide_number} registada em '{notebook_path}'. "
        f"Imagem associada: '{rel_image_path}'."
    )


if __name__ == "__main__":
    mcp.run()


