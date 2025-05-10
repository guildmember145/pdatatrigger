from fastapi import FastAPI
from backend.app.api.endpoints import scan

app = FastAPI()

app.include_router(scan.router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Pdatatrigger API is running"}
