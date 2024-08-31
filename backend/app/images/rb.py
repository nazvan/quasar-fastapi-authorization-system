from uuid import UUID

class RBImage:
    def __init__(self, image_id: UUID | None = None,
                 hoff_id: int | None = None):
        self.id = image_id
        self.hoff_id = hoff_id

    def to_dict(self) -> dict:
        return {key: value for key, value in {
            'id': self.id,
            'hoff_id': self.hoff_id
        }.items() if value is not None}