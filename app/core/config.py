# app/core/config.py
# app/core/config.py
from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    database_url: str
    secret: str = 'secret'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    first_superuser_first_name: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()


# from pathlib import Path
# from pydantic import Field
# from pydantic_settings import BaseSettings, SettingsConfigDict

# class Settings(BaseSettings):
#     app_author: str = Field(default="Tatiana Popova")  # or leave unset and provide via .env
#     db_url: str = Field(default="postgresql://login:password@127.0.0.1:5432/room_reservation")
#     app_path: Path = Field(default_factory=lambda: Path(__file__).resolve().parents[2])
#     app_title: str = Field(default="Бронирование переговорок")
#     database_url: str = Field()
#
#     # pydantic-settings v2 config
#     model_config = SettingsConfigDict(
#         env_file=".env",
#         env_prefix="ROOM_",   # e.g. ROOM_APP_AUTHOR=..., ROOM_DB_URL=...
#         extra="ignore",
#     )
#
# settings = Settings()

