from pydantic import Json
from sqlalchemy.ext.asyncio import AsyncSession

from ...core.models import Questions


class QuestionsCRUD:
    def __init__(self, db_session: AsyncSession, response: Json):
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

    # async def delete_user(self, user_id: UUID) -> Union[UUID, None]:
    #     query = (
    #         update(User)
    #         .where(and_(User.user_id == user_id, User.is_active == True))
    #         .values(is_active=False)
    #         .returning(User.user_id)
    #     )
    #     res = await self.db_session.execute(query)
    #     deleted_user_id_row = res.fetchone()
    #     if deleted_user_id_row is not None:
    #         return deleted_user_id_row[0]

    # async def get_user_by_id(self, user_id: UUID) -> Union[User, None]:
    #     query = select(User).where(User.user_id == user_id)
    #     res = await self.db_session.execute(query)
    #     user_row = res.fetchone()
    #     if user_row is not None:
    #         return user_row[0]
