from sqlalchemy.orm import Session
from dataclasses import dataclass


@dataclass
class RequestHandler:
    db: Session
