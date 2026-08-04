from fastapi import FastAPI
app = FastAPI()
# @app.get("/health")
# def health():
#     return {"status": "ok"}

from database import engine
from sqlalchemy import text

@app.get("/health/db")
def db_health():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"db": "connected"}
    except Exception as e:
        return {"db": "error", "detail": str(e)}