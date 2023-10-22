from fastapi import FastAPI

from .api.routers import router as items

app = FastAPI()
app.include_router(items)


@app.get("/")
async def root():
    return {"message": "200"}
