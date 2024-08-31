from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict

class SImageBase(BaseModel):
    image_name: str = Field(..., description="Имя изображения")
    image_path: str = Field(..., description="Путь к изображению")
    description: Optional[str] = Field(None, description="Описание изображения")
    hoff_id: int = Field(..., description="ID в системе Hoff")

class SImageAdd(SImageBase):
    pass

class SImage(SImageBase):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    upload_time: datetime

class SImageUpdate(BaseModel):
    image_name: Optional[str] = Field(None, description="Новое имя изображения")
    description: Optional[str] = Field(None, description="Новое описание изображения")