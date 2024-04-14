# PDFBuddy 📚

PDFBuddy is a simple yet powerful tool designed to assist users in extracting text from PDF documents and answering questions related to the content of those documents using conversational AI.

## Features

- **PDF Text Extraction**: Easily upload your PDF documents and extract text for further processing.
- **Question Answering**: Ask questions about the uploaded documents, and PDFBuddy will provide relevant answers based on the extracted text.
- **Conversational Interface**: Engage in natural language conversations with PDFBuddy to interactively explore the document content.

## How to Use

1. **Upload PDFs**: Click on the file upload button in the sidebar to upload one or more PDF documents.
2. **Ask Questions**: Type your questions about the content of the uploaded documents in the input field provided.
3. **View Answers**: PDFBuddy will process your question and display relevant answers in the main interface.

## Installation

To run PDFBuddy locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running:
```bash
pip install -r requirements.txt
```
3. Run the application using Streamlit:
```bash
streamlit run app.py
```


## Dependencies

PDFBuddy relies on the following libraries:

- Streamlit: For building the interactive web application.
- PyPDF2: For extracting text from PDF documents.
- HuggingFace Transformers: For language modeling and question answering.
- Other supporting libraries for text processing and handling.

## Contributers
- Naman Sharma 
- Dhruv Bhatia
