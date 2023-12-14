# Yatube Social Network

Этот проект представляет собой социальную сеть, где пользователи могут публиковать посты.

## Модели

- `Post`: Модель для представления постов пользователей. Содержит текст поста, дату публикации, автора и группу.
- `Group`: Модель для представления групп, в которых пользователи могут публиковать свои посты. Содержит название, слаг и описание группы.

## URL-маршруты

- Главная страница (`/`): Показывает последние обновления на сайте.
- Страница группы (`group/<slug:slug>/`): Показывает посты в определенной группе.

## Представления

- `index`: Представление для отображения последних обновлений на сайте.
- `group_posts`: Представление для отображения постов в определенной группе.

## Используемые технологии

- Python: Язык программирования.
- Django: Фреймворк для веб-разработки на Python.

## Автор

Anatolii Bessmertnyi
