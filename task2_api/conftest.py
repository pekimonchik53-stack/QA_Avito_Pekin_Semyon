import pytest
import requests
import random

BASE_URL = "https://qa-internship.avito.com"

@pytest.fixture
def random_seller_id():
    # Генерируем случайный номер продавца, чтобы он не пересекался с другими.
    return random.randint(111111, 999999)

@pytest.fixture
def create_ad(random_seller_id):
    # Создаем объявление и запоминаем его номер.
    url = f"{BASE_URL}/api/1/item"
    payload = {
        "sellerId": random_seller_id,
        "name": "Тестовый котик",
        "price": 1000,
        "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}
    }
    response = requests.post(url, json=payload)
    ad_id = response.json().get("id")
    return random_seller_id, ad_id