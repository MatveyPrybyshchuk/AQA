# AQA
AQA project on python





## Запуск тестов в Docker

1. Проверить, что API-сервер запущен локально на порту 8000.
2. Собрать образ:
   ```bash
   docker build -t my-tests .
3. Использовать команду образ:
   ```bash
   docker run --rm --network=host my-tests pytest -m test_api (или любую другую марку тестов)
