from fastapi import FastAPI
from app.api.v1.router import router

app = FastAPI(title="Food Order System")

app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "ok"}
