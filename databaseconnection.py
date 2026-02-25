from sqlalchemy import create_engine
import os

DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"

if os.getenv("PGSSLCA"):
    DATABASE_URL += (
        f"?sslmode=require"
        f"&sslrootcert={os.getenv('PGSSLCA')}"
        f"&sslcert={os.getenv('PGSSLCERT')}"
        f"&sslkey={os.getenv('PGSSLKEY')}"
    )

engine = create_engine(DATABASE_URL)