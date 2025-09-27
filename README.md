Personalized Destination Explorer

An AI-powered travel recommendation system that helps users discover destinations similar to their preferences — whether it's a dream trip description or a place they love. The system recommends destinations using semantic search, displays real-world images, and plots them on an interactive map.


Features

- **Smart Search**: Choose a known location *or* describe your ideal vacation in plain English.
- **AI Recommendations**: Uses OpenAI Embeddings to semantically find top 5 similar locations.
- **Real Images**: Fetches real-world destination photos via Google Custom Search API.
- **Interactive Map**: Recommended destinations are shown on a zoomable world map.
- **Optional Filters**: Filter by travel theme like "Beach", "Island", "Tropical", etc.
- **Similarity Scores**: Each recommendation includes its semantic similarity score.
- **Secure Config**: All API keys are stored safely using `.env` (not hardcoded).


Tech Stack

| Layer         | Tools / Services                                |
|---------------|--------------------------------------------------|
| Frontend     | Streamlit                                        |
| AI / NLP     | OpenAI Embeddings (`text-embedding-ada-002`)     |
| Semantic Engine | LangChain + Cosine Similarity                  |
| Database     | MySQL (hosted locally or remotely)              |
| Image API    | Google Custom Search API                        |
| Maps         | Folium + streamlit-folium                        |
| Secrets      | Python-dotenv (`.env`) + `.gitignore` secured   |
| Dev Tools    | Git, GitHub, Python 3.9+                         |

Folder Structure

```bash
destination_explorer/
├── app.py                  # Main Streamlit app
├── .env                    # API keys (not uploaded to GitHub)
├── .gitignore              # Ignores venv/, .env, __pycache__
├── requirements.txt        # All dependencies
├── utils/
│   ├── db_connect.py       # MySQL connection
│   ├── data_prep.py        # Load + prepare text for embeddings
│   ├── embeddings.py       # Embedding with OpenAI
│   └── image_fetcher.py    # Fetch images via Google API
├── screenshots/            # App visuals 
├── Data/                   # SQL schema 
│   ├── Locations.sql
│   ├── Feedback.sql
│   └── ...
└── README.md   

Setup Instructions

> You must have a valid OpenAI and Google API Key

1. Clone the repository

```bash
git clone https://github.com/DhikshaMathanagopal/destination_explorer.git
cd destination_explorer

2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate   # Mac/Linux

venv\Scripts\activate.bat  # Windows

3. Install requirements
bash
Copy code
pip install -r requirements.txt

4. Create .env file
Create a .env file in the root directory with:
OPENAI_API_KEY=sk-...your-real-openai-key
GOOGLE_API_KEY=AIza...your-google-key
GOOGLE_CSE_ID=your_custom_search_engine_id

5. Start the app
streamlit run app.py

