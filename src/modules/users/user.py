from dataclasses import dataclass
from src.modules.database.base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


@dataclass
class User(Base):
    __tablename__ = "users"
    user_id: Mapped[str] = mapped_column(
        String, primary_key=True, unique=True, nullable=False)

    username: Mapped[str] = mapped_column(
        String(40), unique=True, nullable=False)

    email: Mapped[str] = mapped_column(
        String(30), unique=True, nullable=False, index=True)

    password: Mapped[str] = mapped_column(String(20), nullable=False)
