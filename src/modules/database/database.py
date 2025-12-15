from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..users.user import User
from .base import Base
engine = create_engine("sqlite:///./sqlite.db",
                       connect_args={"check_same_thread": False}, echo=True, future=True)
session_local = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=Session)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


def init_db():
    Base.metadata.create_all(bind=engine)
