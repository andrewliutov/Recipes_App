## Рецепты

Сервис-помощник для приготовления блюд на основе [CookBook App](https://github.com/andrewliutov/CookBook_App).

Сервис знает некоторое количество рецептов (см. файл `calculator/views.py` — переменная `DATA`).

На запрос вида `/omlet/` отображается список ингредиентов и их количество для приготовления омлета. Аналогично для запроса вида `/pasta/` — список ингредиентов и их количество для приготовления пасты и т.д.

Например:

```
http://127.0.0.1:8000/omlet/

# Ответ
яйца, шт: 2
молоко, л: 0.1
соль, ч.л.: 0.5
```

По умолчанию сервис сообщает количество ингредиентов на одну порцию. Но если передать опциональный параметр `servings` (целое положительное число), то сервис выдает количество ингредиентов на указанное число порций.

Например:

```
http://127.0.0.1:8000/omlet/?servings=4

# Ответ
яйца, шт: 8
молоко, л: 0.4
соль, ч.л.: 2.0
```


#### Документация по проекту

Для запуска проекта необходимо:

- Установить зависимости:

```bash
pip install -r requirements.txt
```

- Выполнить команду:

```bash
python manage.py runserver
```