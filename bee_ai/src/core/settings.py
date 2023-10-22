from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=("./.env.development", "./.env.prod"),
        env_file_encoding="utf-8",
    )

    main_url: str = ""

    db_url: str = ""
    db_echo: bool = False


settings = Settings()
