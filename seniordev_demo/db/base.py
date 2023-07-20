from sqlalchemy.orm import DeclarativeBase

from seniordev_demo.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta
