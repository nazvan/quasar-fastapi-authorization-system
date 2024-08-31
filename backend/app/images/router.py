from fastapi import APIRouter, Depends, HTTPException
from app.images.dao import ImageDAO
from app.images.schemas import SImage, SImageAdd, SImageUpdate
from uuid import UUID

router = APIRouter(prefix='/images', tags=['Работа с изображениями'])

@router.get("/", summary="Получить все изображения")
async def get_all_images() -> list[SImage]:
    return await ImageDAO.find_images()

@router.get("/{image_id}", summary="Получить одно изображение по id")
async def get_image_by_id(image_id: UUID) -> SImage | dict:
    image = await ImageDAO.find_one_or_none(id=image_id)
    if image is None:
        return {'message': f'Изображение с ID {image_id} не найдено!'}
    return image

@router.post("/add/")
async def add_image(image: SImageAdd) -> dict:
    new_image_id = await ImageDAO.add_image(**image.dict())
    if new_image_id:
        return {"message": "Изображение успешно добавлено!", "image_id": new_image_id}
    else:
        return {"message": "Ошибка при добавлении изображения!"}

@router.put("/{image_id}")
async def update_image(image_id: UUID, image_update: SImageUpdate) -> dict:
    updated = await ImageDAO.update(id=image_id, **image_update.dict(exclude_unset=True))
    if updated:
        return {"message": f"Изображение с ID {image_id} обновлено!"}
    else:
        return {"message": "Ошибка при обновлении изображения!"}

@router.delete("/{image_id}")
async def delete_image(image_id: UUID) -> dict:
    deleted = await ImageDAO.delete(id=image_id)
    if deleted:
        return {"message": f"Изображение с ID {image_id} удалено!"}
    else:
        return {"message": "Ошибка при удалении изображения!"}