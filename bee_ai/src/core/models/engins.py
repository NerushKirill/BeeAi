from asyncio import current_task

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)

from bee_ai.src.core.settings import settings


class Engine:
    def __init__(self, db_url: str, echo: bool = False):
        self.engine = create_async_engine(url=db_url, echo=echo, future=True)

        self.session_factory = async_sessionmaker(
            bind=self.engine, autocommit=False, autoflush=False, expire_on_commit=False
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def session_dependency(self) -> AsyncSession:  # type: ignore
        async with self.session_factory() as session:
            yield session
            await session.close()

    async def scoped_session_dependency(self) -> AsyncSession:  # type: ignore
        session = self.get_scoped_session()
        yield session
        await session.close()


engine_prod = Engine(db_url=settings.db_url, echo=settings.db_echo)
