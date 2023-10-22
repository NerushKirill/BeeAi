from sqlalchemy.orm import Mapped

from bee_ai.src.core.models.base import Base


class Questions(Base):
    text_questions: Mapped[str]
    text_answers: Mapped[str]
    date_create: Mapped[str]

    def __str__(self) -> str:
        return "Questions(id=%s, date_create=%s)" % (self.id, self.date_create)

    def __rep__(self) -> str:
        return self.__str__()
