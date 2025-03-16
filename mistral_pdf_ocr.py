from mistralai import Mistral
from pathlib import Path
import os
import base64
from mistralai import DocumentURLChunk
from mistralai.models import OCRResponse

def replace_images_in_markdown(markdown_str: str, images_dict: dict) -> str:
    """
    Replaces image placeholders in Markdown with actual image paths.
    """
    for img_name, img_path in images_dict.items():
        markdown_str = markdown_str.replace(f"![{img_name}]({img_name})", f"![{img_name}]({img_path})")
    return markdown_str

def save_ocr_results(ocr_response: OCRResponse, output_dir: str) -> None:
    """
    Saves OCR results as Markdown and extracted images.
    """
    # Create output directories
    os.makedirs(output_dir, exist_ok=True)
    images_dir = os.path.join(output_dir, "images")
    os.makedirs(images_dir, exist_ok=True)
    
    all_markdowns = []
    for page in ocr_response.pages:
        # Save images
        page_images = {}
        for img in page.images:
            img_data = base64.b64decode(img.image_base64.split(',')[1])
            img_path = os.path.join(images_dir, f"{img.id}.png")
            with open(img_path, 'wb') as f:
                f.write(img_data)
            page_images[img.id] = f"images/{img.id}.png"
        
        # Process Markdown content
        page_markdown = replace_images_in_markdown(page.markdown, page_images)
        all_markdowns.append(page_markdown)
    
    # Save complete Markdown file
    with open(os.path.join(output_dir, "complete.md"), 'w', encoding='utf-8') as f:
        f.write("\n\n".join(all_markdowns))

def process_pdf(pdf_path: str, api_key: str) -> None:
    """
    Processes a PDF file with Mistral OCR.
    """
    # Initialize the Mistral client
    client = Mistral(api_key=api_key)
    
    # Check if the PDF file exists
    pdf_file = Path(pdf_path)
    if not pdf_file.is_file():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    # Create an output directory name
    output_dir = f"ocr_results_{pdf_file.stem}"
    
    # Upload and process the PDF
    uploaded_file = client.files.upload(
        file={
            "file_name": pdf_file.stem,
            "content": pdf_file.read_bytes(),
        },
        purpose="ocr",
    )
    
    signed_url = client.files.get_signed_url(file_id=uploaded_file.id, expiry=1)
    pdf_response = client.ocr.process(
        document=DocumentURLChunk(document_url=signed_url.url), 
        model="mistral-ocr-latest", 
        include_image_base64=True
    )
    
    # Save results
    save_ocr_results(pdf_response, output_dir)
    print(f"OCR processing complete. Results saved in: {output_dir}")

if __name__ == "__main__":
    # Example usage
    API_KEY = "your key"
    PDF_PATH = "document.pdf"
    
    process_pdf(PDF_PATH, API_KEY)
