import httpx
from fastapi import APIRouter

from .schemas import Item

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def read_public_api(item: Item):
    async with httpx.AsyncClient() as client:
        r = await client.get(
            f"https://jservice.io/api/random?count={item.questions_num}"
        )
        return r.json()
