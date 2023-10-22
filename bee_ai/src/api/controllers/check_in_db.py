from pydantic import Json
from sqlalchemy.ext.asyncio import AsyncSession

from .crud_items import QuestionsCRUD
from ...core.models import Questions
from .schemas import Item


# TODO add shema for response -> self.response.id
async def check_question(engine: AsyncSession, question: Json):
    if QuestionsCRUD(engine, question).get_question_by_id():
        return question


async def add_question(engine: AsyncSession, question: Json):
    if QuestionsCRUD(engine, question).create_question():
        return question


async def get_question_last(item: Item) -> Questions | None:
    # show item.questions_num
    pass
