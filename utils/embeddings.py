from langchain_community.embeddings import OpenAIEmbeddings
from config import OPENAI_API_KEY

def embed_text_list(text_list):
    """
    Generate embeddings using OpenAI Embeddings (via LangChain).
    """
    try:
        embedder = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY, model="text-embedding-ada-002")
        vectors = embedder.embed_documents(text_list)
        return vectors
    except Exception as e:
        print("❌ Embedding failed:", e)
        return []
