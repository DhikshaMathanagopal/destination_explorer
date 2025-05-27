from utils.data_prep import load_location_text

print("🟢 Testing location text loading...")

df = load_location_text()

if df is None or df.empty:
    print("❌ DataFrame is empty or not returned at all!")
else:
    print("✅ DataFrame loaded with", len(df), "rows.")
    print(df.head(3)[['LocationID', 'text']])
