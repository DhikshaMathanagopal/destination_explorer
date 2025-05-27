# run_full_pipeline.py

from utils.data_prep import load_location_text
from utils.embeddings import embed_text_list
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

print("🔌 Starting full pipeline...")

# 1. Load and prepare data
print("📥 Loading and preparing data...")
df = load_location_text()

print("\n✅ DataFrame loaded.")
print("🔢 Number of records:", len(df))
print(df.head())

# Safety checks
if len(df) == 0:
    print("❌ ERROR: No data loaded from the database.")
    exit()

if 'text' not in df.columns:
    print("❌ ERROR: 'text' column is missing from the DataFrame.")
    exit()

if df['text'].isnull().all():
    print("❌ ERROR: All text entries are empty. Check data_prep.py.")
    exit()

# Preview text
print("\n📌 First few texts for embedding preview:")
for i in range(min(3, len(df))):
    print(f" - {df.iloc[i]['LocationID']}: {df.iloc[i]['text'][:100]}")

# 2. Generate embeddings
print("\n🔁 Generating embeddings from OpenAI...")
texts = df['text'].tolist()

embeddings = embed_text_list(texts)

if not embeddings:
    print("❌ Embedding generation failed. Exiting.")
    exit()

print("✅ Total embeddings generated:", len(embeddings))

# 3. Compute cosine similarity matrix
print("📊 Computing cosine similarity...")
similarity_matrix = cosine_similarity(embeddings)

# 4. Pick a reference location
reference_index = 0  # Change to any index you want to test
ref_location = df.iloc[reference_index]

print(f"\n🎯 Top 5 places similar to: {ref_location['LocationID']}")
print("🔍 Description Preview:", ref_location['text'][:100] + "...")

# 5. Get top 5 most similar locations (excluding self)
similarities = list(enumerate(similarity_matrix[reference_index]))
similarities = sorted(similarities, key=lambda x: x[1], reverse=True)[1:6]  # skip self-match

print("\n📍 Recommended Similar Locations:\n")
for idx, score in similarities:
    loc = df.iloc[idx]
    print(f"🔹 {loc['LocationID']} (Score: {round(score, 3)})")
    print(f"   📘 {loc['text'][:100]}...\n")

print("✅ Done.")
