# Mistral-Powered-OCR-PDF-Processing-Tool
This project is a **simple yet powerful tool** for processing PDF files using **Mistral AI's OCR (Optical Character Recognition)** capabilities. It extracts **text** and **images** from PDF documents and saves the results in **Markdown format**.  

---

## **🔹 Features**  
✅ Process PDF files using **Mistral AI's OCR**  
✅ Automatically extract **text** while preserving the original layout  
✅ Extract and **save images** from the PDF  
✅ Generate a **complete Markdown file** with all extracted content  
✅ Supports **multiple languages**, including Chinese  

---

## **🔹 Installation Requirements**  
To run this tool, install the following dependency:  

```bash
pip install mistralai
```

---

## **🔹 How to Use**  

### **1️⃣ Get Your Mistral AI API Key**  
You need a **Mistral AI API key** to use this tool.  

### **2️⃣ Modify `mistral_pdf_ocr.py`**  
Update the **API key** and **PDF file path** in the script:  

```python
API_KEY = "your_mistral_api_key"
PDF_PATH = "your_pdf_file.pdf"
```

### **3️⃣ Run the Script**  
Execute the script to process the PDF:  

```bash
python mistral_pdf_ocr.py
```

---

## **🔹 Output Results**  
After running the script, a new folder named **`ocr_results_[PDF filename]`** will be created in your working directory. It contains:  

📄 **`complete.md`** → A Markdown file with extracted text  
📂 **`images/`** → A folder containing all extracted images  

---

## **🔹 Notes**  
⚠ Ensure the **PDF file path** is correct  
⚠ Your **API key** must have **OCR access**  
