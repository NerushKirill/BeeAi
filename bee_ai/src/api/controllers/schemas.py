from pydantic import BaseModel, PositiveInt


class Item(BaseModel):
    questions_num: PositiveInt


# class Question(BaseModel):
#     id: int
#     text_answers: str
#     ext_questions: str
#     date_create: str
