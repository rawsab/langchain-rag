from pdf_extract import extract_text_from_pdf
from doc_indexer import DocumentIndexer


indexer = DocumentIndexer("openai-api-key")

def process_pdf(pdf_path):
    pdf_text = extract_text_from_pdf(pdf_path)
    indexer.index_documents([pdf_text])

def query_pdf(query):
    return indexer.search_documents(query)

def main():
    sample_pdf_path = "test.pdf" # add path to test PDF
    example_query = "" # add query for testing

    process_pdf(sample_pdf_path)

    results = query_pdf(example_query)
    print("Query Results:", results)

if __name__ == "__main__":
    main()
