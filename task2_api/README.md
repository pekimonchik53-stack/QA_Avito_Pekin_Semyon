# QA Avito Пекин Семён

## Задание 1: Скриншот с багами

Список багов находится в файле `list_of_bugs.md` в папке task_1.

---

## Задание 2.1: API тесты

### Как скачать и запустить тесты

#### 1. Скачать репозиторий через терминал

```
git clone https://github.com/pekimonchik53-stack/QA_Avito_Pekin_Semyon.git
cd QA_Avito_Pekin_Semyon/task2_api
```
#### 2. Установить Python, если его нет на устройстве
```
Скачать с python.org.
```
#### 3. Установить зависимости
```
pip install -r requirements.txt
Если файла requirements.txt нет:
pip install requests pytest
```
#### 4. Запустить тесты
```
pytest test_ads.py -v
```
#### 5. Ожидаемый результат
```
Все тесты будут зелеными (PASSED) или красными (FAILED), последнее это баги,
их описание в BUGS.md:
test_ads.py::test_create_ad FAILED                                                                               [  6%]
test_ads.py::test_get_ad_by_id FAILED                                                                            [ 13%]
test_ads.py::test_get_ads_by_seller_id PASSED                                                                    [ 20%]
test_ads.py::test_get_statistics FAILED                                                                          [ 26%]
test_ads.py::test_create_ad_no_seller_id FAILED                                                                  [ 33%]
test_ads.py::test_get_nonexistent_ad PASSED                                                                      [ 40%]
test_ads.py::test_create_ad_idempotency FAILED                                                                   [ 46%]
test_ads.py::test_create_ad_with_empty_name PASSED                                                               [ 53%]
test_ads.py::test_create_ad_with_negative_price PASSED                                                           [ 60%]
test_ads.py::test_create_ad_with_zero_price PASSED                                                               [ 66%]
test_ads.py::test_create_ad_with_huge_price PASSED                                                               [ 73%]
test_ads.py::test_create_ad_with_long_name PASSED                                                                [ 80%]
test_ads.py::test_create_ad_no_name PASSED                                                                       [ 86%]
test_ads.py::test_create_ad_no_price PASSED                                                                      [ 93%]
test_ads.py::test_create_ad_no_statistics PASSED   
```