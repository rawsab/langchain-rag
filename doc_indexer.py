from openai import OpenAI
from chroma import Chroma

# Handles document embedding and indexing
class DocumentIndexer:
    # initialize with OpenAI API key
    def __init__(self, openai_api_key):
        self.openai = OpenAI(api_key=openai_api_key)
        self.chroma = Chroma()

    # generate embedding
    def get_embedding(self, text):
        response = self.openai.Embeddings.create(
            input=text,
            model="text-embedding-ada-002"
        )
        return response['data']

    # index list of texts by embedding and adding to Chroma
    def index_documents(self, texts):
        for text in texts:
            embedding = self.get_embedding(text)
            self.chroma.add_document(text, embedding)

    # search indexed documents based on query
    def search_documents(self, query):
        query_embedding = self.get_embedding(query)
        results = self.chroma.search(query_embedding)
        return results
