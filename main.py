import os
import re

import fitz
from markdownify import markdownify as md


def pdf_to_text_with_formatting(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)

        # Obtener el texto manteniendo el formato base
        page_text = page.get_text("text")

        # Usar una expresión regular para añadir un salto de línea antes de los números seguidos de un punto
        page_text = re.sub(r'(\d+\.)', r'\n\1', page_text)

        text += page_text

    return text


def text_to_markdown(text):
    markdown_text = md(text, heading_style="ATX")  # Encabezados estilo ATX (con #)
    return markdown_text


def pdf_to_markdown(pdf_path, markdown_path):
    text = pdf_to_text_with_formatting(pdf_path)
    markdown_text = text_to_markdown(text)
    with open(markdown_path, "w", encoding="utf-8") as md_file:
        md_file.write(markdown_text)


pdf_directory = "./"

for archivo in os.listdir(pdf_directory):
    if archivo.lower().endswith('.pdf'):
        pdf_path = os.path.join(pdf_directory, archivo)
        markdown_path = os.path.join(pdf_directory, archivo[:-4] + '.md')
        print(f"Convirtiendo {archivo} a {markdown_path}")
        pdf_to_markdown(pdf_path, markdown_path)