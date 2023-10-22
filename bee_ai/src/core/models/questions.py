from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Questions(Base):
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    text_answers: Mapped[str]
    text_questions: Mapped[str]
    date_create: Mapped[str]

    def __str__(self) -> str:
        return "Questions(id=%s, date_create=%s)" % (self.id, self.date_create)

    def __rep__(self) -> str:
        return self.__str__()
