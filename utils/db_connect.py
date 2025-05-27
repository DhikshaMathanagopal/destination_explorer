from sqlalchemy import create_engine
from config import DB_CONFIG

def get_connection():
    """
    Establishes and returns a SQLAlchemy engine to connect to the MySQL database.
    """
    try:
        url = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['database']}"
        engine = create_engine(url)
        print("✅ Database connection established.")
        return engine
    except Exception as e:
        print("❌ Failed to connect to database:", e)
        return None