from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text
from app.database import Base, str_uniq, uuid_pk
from datetime import datetime
from uuid import UUID

class Image(Base):
    __tablename__ = "images"

    id: Mapped[uuid_pk]
    image_name: Mapped[str_uniq]
    image_path: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    upload_time: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    hoff_id: Mapped[int] = mapped_column(nullable=False)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, image_name={self.image_name!r})"

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": str(self.id),  # Преобразуем UUID в строку
            "image_name": self.image_name,
            "image_path": self.image_path,
            "description": self.description,
            "upload_time": self.upload_time,
            "hoff_id": self.hoff_id
        }