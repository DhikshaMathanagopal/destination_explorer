from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def get_top_k_similar(embedding_vectors, k=5, reference_index=0):
    """
    Computes cosine similarity and returns top K similar locations to the reference_index.
    """
    similarity_matrix = cosine_similarity(embedding_vectors)
    scores = list(enumerate(similarity_matrix[reference_index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    
    # Skip self match
    return scores[1:k+1]
