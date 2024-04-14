# PDFBuddy 📚

PDFBuddy is a simple yet powerful tool designed to assist users in extracting text from PDF documents and answering questions related to the content of those documents using conversational AI.

## Features

- **PDF Text Extraction**: Easily upload your PDF documents and extract text for further processing.
- **Question Answering**: Ask questions about the uploaded documents, and PDFBuddy will provide relevant answers based on the extracted text.
- **Conversational Interface**: Engage in natural language conversations with PDFBuddy to interactively explore the document content.

## How it Works

1. PDF Loading: The app reads multiple PDF documents and extracts their text content.
2. Text Chunking: The extracted text is divided into smaller chunks that can be processed effectively.
3. Language Model: The application utilizes a language model to generate vector representations (embeddings) of the text chunks.
4. Similarity Matching: When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones.
5. Response Generation: The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDFs.

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
