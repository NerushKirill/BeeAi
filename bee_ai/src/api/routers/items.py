from fastapi import APIRouter

from ...core.settings import settings
from ..controllers import Item, get_items

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


@router.post(settings.main_url)
async def read_public_api(item: Item):
    r = await get_items(item)
    for i in r:
        print(
            i["id"],
            i["answer"],
            i["question"],
            i["created_at"],
        )
    return r
