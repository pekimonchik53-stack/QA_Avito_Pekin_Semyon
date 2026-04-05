# pytest test_ads.py -v
import requests
from conftest import BASE_URL

# 1. Проверка создания объявления
def test_create_ad(random_seller_id):
    url = f"{BASE_URL}/api/1/item"
    payload = {
        "sellerId": random_seller_id,
        "name": "Пушистый кот",
        "price": 5000,
        "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == "Пушистый кот"
    assert data["price"] == 5000

# 2. Проверка получения объявления по его номеру
def test_get_ad_by_id(create_ad):
    seller_id, ad_id = create_ad
    url = f"{BASE_URL}/api/1/item/{ad_id}"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    if isinstance(data, list):
        data = data[0]
    assert data["id"] == ad_id
    assert data["sellerId"] == seller_id

# 3. Проверка поиск по продавцу
def test_get_ads_by_seller_id(create_ad):
    seller_id, _ = create_ad
    url = f"{BASE_URL}/api/1/{seller_id}/item"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for ad in data:
        assert ad["sellerId"] == seller_id

# 4. Проверка статистики
def test_get_statistics(create_ad):
    _, ad_id = create_ad
    url = f"{BASE_URL}/api/1/statistic/{ad_id}"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    if isinstance(data, list):
        data = data[0]
    assert "likes" in data
    assert "viewCount" in data
    assert "contacts" in data

# 5. Создание без sellerId
def test_create_ad_no_seller_id():
    url = f"{BASE_URL}/api/1/item"
    payload = {
        "name": "Котик без продавца",
        "price": 1000,
        "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}
    }
    response = requests.post(url, json=payload)
    assert response.status_code in [400, 500]

# 6. Получение несуществующего объявления
def test_get_nonexistent_ad():
    fake_id = "00000000-0000-0000-0000-000000000000"
    url = f"{BASE_URL}/api/1/item/{fake_id}"
    response = requests.get(url)
    assert response.status_code == 404

# 7. Идемпотентность создания
def test_create_ad_idempotency(random_seller_id):
    url = f"{BASE_URL}/api/1/item"
    payload = {
        "sellerId": random_seller_id,
        "name": "Одинаковый кот",
        "price": 1000,
        "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}
    }
    response1 = requests.post(url, json=payload)
    response2 = requests.post(url, json=payload)
    assert response1.status_code == 200
    assert response2.status_code == 200
    id1 = response1.json().get("id")
    id2 = response2.json().get("id")
    assert id1 != id2

# 8. Создание с пустым name
def test_create_ad_with_empty_name(random_seller_id):
    url = f"{BASE_URL}/api/1/item"
    payload = {
        "sellerId": random_seller_id,
        "name": "",
        "price": 1000,
        "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}
    }
    response = requests.post(url, json=payload)
    assert response.status_code in [400, 500]

# 9. Создание с отрицательной ценой
def test_create_ad_with_negative_price(random_seller_id):
    url = f"{BASE_URL}/api/1/item"
    payload = {
        "sellerId": random_seller_id,
        "name": "Котик с отрицательной ценой",
        "price": -1000,
        "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}
    }
    response = requests.post(url, json=payload)
    assert response.status_code in [400, 500]

#10. Создание с нулевой ценой
def test_create_ad_with_zero_price(random_seller_id):
    url = f"{BASE_URL}/api/1/item"
    payload = {
        "sellerId": random_seller_id,
        "name": "Котик с нулевой ценой",
        "price": 0,
        "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}
    }
    response = requests.post(url, json=payload)
    assert response.status_code in [200, 400]

# 11. Создание с очень большой ценой
def test_create_ad_with_huge_price(random_seller_id):
    url = f"{BASE_URL}/api/1/item"
    payload = {
        "sellerId": random_seller_id,
        "name": "Котик за миллиард",
        "price": 999999999,
        "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}
    }
    response = requests.post(url, json=payload)
    assert response.status_code in [200, 400]

# 12. Создание с очень длинным именем
def test_create_ad_with_long_name(random_seller_id):
    url = f"{BASE_URL}/api/1/item"
    payload = {
        "sellerId": random_seller_id,
        "name": "А" * 1000,
        "price": 1000,
        "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}
    }
    response = requests.post(url, json=payload)
    assert response.status_code in [200, 400]

# 13. Создание без поля name
def test_create_ad_no_name(random_seller_id):
    url = f"{BASE_URL}/api/1/item"
    payload = {
        "sellerId": random_seller_id,
        "price": 1000,
        "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}
    }
    response = requests.post(url, json=payload)
    assert response.status_code in [400, 500]

# 14. Создание без поля price
def test_create_ad_no_price(random_seller_id):
    url = f"{BASE_URL}/api/1/item"
    payload = {
        "sellerId": random_seller_id,
        "name": "Котик без цены",
        "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}
    }
    response = requests.post(url, json=payload)
    assert response.status_code in [400, 500]

# 15. Создание без statistics
def test_create_ad_no_statistics(random_seller_id):
    url = f"{BASE_URL}/api/1/item"
    payload = {
        "sellerId": random_seller_id,
        "name": "Котик без статистики",
        "price": 1000
    }
    response = requests.post(url, json=payload)
    assert response.status_code in [400, 500]