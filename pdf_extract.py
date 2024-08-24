import pdfplumber

# Simple function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    
    text_content = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text_content.append(page.extract_text())
            
    return "\n".join(text_content)
