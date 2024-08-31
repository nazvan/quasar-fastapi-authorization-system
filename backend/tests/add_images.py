import requests
import uuid
import random

BASE_URL = "http://localhost:8000"  # Замените на ваш базовый URL

def test_add_image():
    image_data = {
        "image_name": "test_image.jpg",
        "image_path": "https://picsum.photos/200/300",
        "description": "Тестовое изображение",
        "hoff_id": 12345
    }
    response = requests.post(f"{BASE_URL}/images/add/", json=image_data)
    assert response.status_code == 200
    assert "image_id" in response.json()
    return response.json()["image_id"]

def test_get_image(image_id):
    response = requests.get(f"{BASE_URL}/images/{image_id}")
    assert response.status_code == 200
    assert response.json()["id"] == image_id

def test_update_image(image_id):
    update_data = {
        "image_path": "https://picsum.photos/300/400"
    }
    response = requests.put(f"{BASE_URL}/images/{image_id}", json=update_data)
    assert response.status_code == 200
    assert "обновлено" in response.json()["message"]

def test_delete_image(image_id):
    response = requests.delete(f"{BASE_URL}/images/{image_id}")
    assert response.status_code == 200
    assert "удалено" in response.json()["message"]

def add_random_images(count=5):
    added_images = []
    for i in range(count):
        image_data = {
            "image_name": f"random_image_{i}.jpg",
            "image_path": f"https://picsum.photos/{random.randint(200, 500)}/{random.randint(200, 500)}",
            "description": f"Случайное изображение {i}",
            "hoff_id": random.randint(10000, 99999)
        }
        response = requests.post(f"{BASE_URL}/images/add/", json=image_data)
        if response.status_code == 200:
            added_images.append(response.json()["image_id"])
    return added_images

if __name__ == "__main__":
    # Тестирование добавления, получения, обновления и удаления одного изображения
    # image_id = test_add_image()
    # test_get_image(image_id)
    # test_update_image(image_id)
    # test_delete_image(image_id)

    # Добавление 5 случайных изображений
    random_image_ids = add_random_images(5)
    print(f"Добавлено {len(random_image_ids)} случайных изображений с ID: {random_image_ids}")

    # Получение всех изображений
    response = requests.get(f"{BASE_URL}/images/")
    print(f"Всего изображений в базе: {len(response.json())}")