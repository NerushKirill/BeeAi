import httpx
from pydantic import Json

from .schemas import Item


async def get_items(item: Item) -> Json:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://jservice.io/api/random?count={item.questions_num}"
        )
        return response.json()
