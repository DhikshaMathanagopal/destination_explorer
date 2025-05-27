from utils.db_connect import get_connection

engine = get_connection()

if engine:
    with engine.connect() as connection:
        result = connection.execute("SHOW TABLES;")
        print("📦 Tables in database:")
        for row in result:
            print("  -", row[0])