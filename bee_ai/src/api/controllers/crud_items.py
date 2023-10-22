from pydantic import Json

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ...core.models import Questions


# TODO add shema for response -> self.response.id
class QuestionsCRUD:
    def __init__(self, db_session: AsyncSession, response: Json):  # not Json
        self.db_session = db_session
        self.response = response

    async def create_question(self):
        new_question = Questions(
            id=self.response["id"],
            text_answers=self.response["answer"],
            ext_questions=self.response["question"],
            date_create=self.response["created_at"],
        )
        self.db_session.add(new_question)

        await self.db_session.flush()
        return new_question

    async def get_question_by_id(self) -> Questions | None:
        query = select(Questions).where(Questions.id == self.response["id"])
        result = await self.db_session.execute(query)
        question = result.fetchone()
        if question is not None:
            return question[0]
