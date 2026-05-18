import psycopg 

def get_connection():
    conn = psycopg.connect("postgresql://postgres.zpxomggkknwfkpqrziqv:A01012837186A@aws-1-eu-central-2.pooler.supabase.com:6543/postgres")

    return conn

print("Database connection established successfully.")  