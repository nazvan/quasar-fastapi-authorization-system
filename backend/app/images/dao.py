from app.dao.base import BaseDAO
from app.images.models import Image
from app.database import async_session_maker
from sqlalchemy.future import select

class ImageDAO(BaseDAO):
    model = Image

    @classmethod
    async def find_images(cls, **image_data):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**image_data)
            result = await session.execute(query)
            images = result.scalars().all()
            return [image.to_dict() for image in images]

    @classmethod
    async def add_image(cls, **image_data):
        async with async_session_maker() as session:
            async with session.begin():
                new_image = cls.model(**image_data)
                session.add(new_image)
                await session.flush()
                new_image_id = new_image.id
                await session.commit()
                return new_image_id