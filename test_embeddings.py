from utils.data_prep import load_location_text
from utils.embeddings import embed_text_list
import numpy as np

print("🔁 Loading and embedding location texts...")
df = load_location_text()

if df.empty:
    print("❌ No data loaded!")
    exit()

texts = df['text'].tolist()
vectors = embed_text_list(texts)

if not vectors:
    print("❌ Embedding failed.")
    exit()

print(f"✅ {len(vectors)} embeddings generated.")
print("🔎 Sample vector length:", len(vectors[0]))
print("📘 Sample preview:", df.iloc[0]['text'][:100])