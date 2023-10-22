from fastapi import FastAPI

from .core.settings import settings
from .api.routers import router as items

app = FastAPI()
app.include_router(items)


@app.get(settings.main_url)
async def root():
    return {"message": "200"}
