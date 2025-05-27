from sqlalchemy import text
import pandas as pd
from utils.db_connect import get_connection

def assign_category(description):
    """Infer category based on description keywords."""
    description = description.lower()
    if "beach" in description or "lagoon" in description:
        return "Beach"
    elif "island" in description or "tropical" in description:
        return "Island"
    elif "temple" in description or "ruins" in description or "heritage" in description:
        return "Historic"
    elif "mountain" in description or "trek" in description or "hike" in description:
        return "Adventure"
    elif "city" in description or "urban" in description:
        return "Urban"
    else:
        return "Other"

def load_location_text():
    engine = get_connection()
    if engine is None:
        print("❌ DB connection failed.")
        return None

    query = text("""
        SELECT 
            l.LocationID, 
            l.Name, 
            l.Description, 
            l.Latitude, 
            l.Longitude,
            f.Comments AS Feedback,
            l.Country
        FROM 
            Locations l
        LEFT JOIN 
            Feedback f ON l.LocationID = f.LocationID
    """)

    try:
        df = pd.read_sql(query, engine)
    except Exception as e:
        print("❌ SQL read failed:", e)
        return None

    df = df.fillna("")
    df["InferredCategory"] = df["Description"].apply(assign_category)

    df["text"] = (
        df["Name"] + ". " +
        df["Description"] + ". " +
        "Category: " + df["InferredCategory"] + ". " +
        "Feedback: " + df["Feedback"]
    )

    return df[["LocationID", "Name", "Description", "InferredCategory", "Feedback", "Country", "Latitude", "Longitude", "text"]]