from fastapi import APIRouter

import asyncio

from ...core.settings import settings
from ...core.models import engine_prod
from ..controllers import Item, get_items, check_question, add_question

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


@router.post(settings.main_url)
async def read_public_api(item: Item):
    answer = await get_items(item)
    not_in_db = []

    for question in answer:
        # result = await check_question(engine_prod.session_dependency(), question)
        not_in_db.append(
            await check_question(engine_prod.session_dependency(), question)
        )

    for question in not_in_db:
        await add_question(engine_prod.session_dependency(), question)

    return not_in_db
