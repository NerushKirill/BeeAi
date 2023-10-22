from pydantic import BaseModel, PositiveInt


class Item(BaseModel):
    questions_num: PositiveInt
