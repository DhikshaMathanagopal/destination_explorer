import streamlit as st
import pandas as pd
import folium
from sklearn.metrics.pairwise import cosine_similarity
from streamlit_folium import st_folium

from utils.data_prep import load_location_text
from utils.embeddings import embed_text_list
from utils.image_fetcher import fetch_image_url

st.set_page_config(page_title="Personalized Destination Explorer", layout="wide")
st.title("🌍 Personalized Destination Explorer")

# Load location data
with st.spinner("Loading locations from database..."):
    df = load_location_text()
    if df is None or df.empty:
        st.error("❌ Failed to load locations.")
        st.stop()

# Generate embeddings
with st.spinner("Generating semantic vectors with OpenAI embeddings..."):
    embeddings = embed_text_list(df["text"].tolist())

# Sidebar filters
st.sidebar.header("🧭 Filters")
filter_text = st.sidebar.text_input("Filter by Inferred Category (optional)", placeholder="Island, Beach, Tropical")

# UI Inputs
col1, col2 = st.columns([1, 2])
selected_id = col1.selectbox("Choose a location you liked", [""] + df["Name"].tolist())
user_input = col2.text_input("Or describe your dream trip:")

# Ensure only one input method is active
if selected_id and user_input:
    st.warning("⚠️ Please use only one option: either select a location or describe your trip.")
    st.stop()
elif not selected_id and not user_input:
    st.info("ℹ️ Please select a location or describe your dream trip to get recommendations.")
    st.stop()

# Core similarity logic
def get_top_k_similar(embedding_matrix, reference_index=None, query_vector=None, k=5):
    if query_vector is not None:
        similarities = cosine_similarity([query_vector], embedding_matrix)[0]
    else:
        similarities = cosine_similarity([embedding_matrix[reference_index]], embedding_matrix)[0]

    scored = list(enumerate(similarities))
    scored = sorted(scored, key=lambda x: x[1], reverse=True)

    top_results = []
    for idx, score in scored:
        if idx == reference_index:
            continue
        loc = df.iloc[idx]
        if filter_text and filter_text.lower() not in loc["InferredCategory"].lower():
            continue
        if reference_index is not None and loc["InferredCategory"] == df.iloc[reference_index]["InferredCategory"]:
            score += 0.02
        top_results.append((idx, score))
        if len(top_results) == k:
            break
    return top_results

# Generate recommendations
if user_input:
    input_vector = embed_text_list([user_input])[0]
    top_results = get_top_k_similar(embeddings, query_vector=input_vector)
    reference_text = f"🧠 Based on your input: _{user_input}_"
else:
    ref_idx = df[df["Name"] == selected_id].index[0]
    top_results = get_top_k_similar(embeddings, reference_index=ref_idx)
    reference_text = f"📍 Based on: _{df.iloc[ref_idx]['Name']}_"

# 🔍 Recommendations Section
st.markdown("### 🖼️ Image Preview")

cols = st.columns(len(top_results))
for i, (col, (idx, score)) in enumerate(zip(cols, top_results)):
    loc = df.iloc[idx]
    image_url = fetch_image_url(loc["Name"])
    if image_url:
        with col:
            st.image(image_url, caption=loc["Name"], use_container_width=True)

st.markdown("### 🔍 AI Recommended Destinations")
st.markdown(reference_text)

for idx, score in top_results:
    loc = df.iloc[idx]
    st.markdown(f"#### 📌 {loc['Name']} (Similarity Score: {round(score, 3)})")
    st.markdown(f"**Category:** {loc['InferredCategory']}")
    st.markdown(f"{loc['text']}\n")

# 🗺️ Map Section
st.markdown("### 🗺 Map View of Recommendations")
m = folium.Map(location=[df["Latitude"].mean(), df["Longitude"].mean()], zoom_start=2)

for idx, score in top_results:
    loc = df.iloc[idx]
    folium.Marker(
        location=[loc["Latitude"], loc["Longitude"]],
        popup=f"{loc['Name']} ({round(score, 3)})",
        icon=folium.Icon(color='green')
    ).add_to(m)

st_folium(m, width=700, height=500)
