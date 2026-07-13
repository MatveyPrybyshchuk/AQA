# AQA
AQA project on python

# Дипломный проект 

## Активировать .venv
.\.venv\Scripts\Activate.ps1   

## Установка всех пакетов

Установите всё разом:

```bash
pip install -r requirements.txt
```


## Запуск первого теста

Запуск тестов:

```bash
pytest -q
```

## Запуск первого теста с разными ключами

**Базовые:**

```bash
pytest          # стандартный вывод
pytest -v       # подробные имена тестов
pytest -q       # тихий режим
pytest tests/test_pytest/test_intro.py -v -s --cache-clear --tb=short  # пример
```

Полезные флаги на практике
```bash
#-s — не захватывать stdout/stderr (удобно для дебага print)
#--lf — запустить только “упавшие” на прошлом прогоне
#--ff — сначала упавшие, потом остальные
#--durations=10 — показать 10 самых долгих тестов
```bash

**Отбор тестов:**

```bash
pytest tests/test_python_org_wait.py   # один файл
pytest tests -k search                 # по подстроке в имени
pytest -k "not e2e"                    # исключить
```

**Маркеры:**

```python
import pytest

@pytest.mark.e2e
def test_something():
    ...
```

Запуск по маркеру:

```bash
pytest -m e2e
```

**Поведение при падениях и отчёты:**

```bash
pytest -x            # стоп на первом фейле
pytest --maxfail=1   # то же
pytest -ra           # причины skip/xfail
pytest -s            # показать print()/stdout
```


```bash
allure serve .allure-results

pytest -m test_auth --alluredir=.allure-results
allure generate .allure-results -o .allure-report
allure open .allure-report
```



## Запуск тестов в Docker

1. Проверить, что API-сервер запущен локально на порту 8000. и докер запущен
2. Собрать образ:
   ```bash
   docker build -t my-tests .
3. Использовать команду образ:
   ```bash
   запускает тесты и удаляет образ
   docker run --rm -v ${PWD}/.allure-results:/app/.allure-results my-tests

   открыть отчет
   allure serve ./.allure-results

   удалить созданный образ
   docker rmi my-tests
