## Запуск проекта
### 1.
```python
openai_adapter.py

openai.api_key = 'API KEY'  # Вставляем ключ
```
### 2.
```text
TERMINAL:

>>> Введите запрос: ВВОДИТЕ СВОЙ ЗАПРОС 

(Для того, чтобы прекратить - напишите /q)
```

## Архитектура проекта:
```text
edx_openai
    |
    | - src
    |    |- adapters
    |    |     | - __init__.py
    |    |     | - edx_adapter.py (адаптер EDX API)
    |    |     | - openai_adapter.py (адаптер ChatGPT)
    |    |  
    |    | - domain
    |    |     | - __init__.py 
    |    |     | - model.py (модель, которая подсоединяет все адаптеры)
    | - main.py (запуск модели с адаптерами)
    .gitignore
    README.md (документация репозитория)
    requirements.txt (нужные библиотеки для проекта)
```
