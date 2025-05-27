from utils.embeddings import embed_text_list
from utils.data_prep import load_location_text
from utils.recommender import get_top_k_similar

print("🔁 Loading and embedding location texts...")
df = load_location_text()
vectors = embed_text_list(df["text"].tolist())

print("📌 Finding similar locations to LocationID:", df.loc[0, "LocationID"])
top_similars = get_top_k_similar(vectors, k=5, reference_index=0)

for idx, score in top_similars:
    print(f"{df.loc[idx, 'LocationID']} (score: {round(score, 3)}): {df.loc[idx, 'text'][:60]}...")
