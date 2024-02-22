# Statistics

Cистема учета и анализа данных, поступающих с условного устройства. Полученные данные привязываются к временной метке и устройству, с которого пришли данные, и сохраняются в БД. Набор данных используется для дальнейшего анализа.

## Технологический стек

- Python 3.9
- **Веб-фреймворк:** FastApi
- SQLAlchemy
- Alembic
- Uvicorn

## Устройства 
В данном сервисе может быть несколько устройств. У каждого устройства есть название и идентификатор. Также предусмотрено хранение пользователя устройства. Каждый пользователь может создать устройство. 

## Данные 

У данных есть дата создания, а также индентификатор устройства, с которого пришли данные. Отправка данных доступна всем пользователям.

## Пользователи

Пользователи представлены при помощи библиотеки FastAPI Users. Транспорт Bearer и стратегия JWT.
Каждый пользователь может просмотреть все данные и все утройства, а также создать устройство, добавить данные и получить анализ статистики.

## Запуск проекта

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:ibonish/Statistics.git
```

```
cd Statistics
```

Собрать образ:

```
docker build -t statimage .
```

Запустить контейнер:

```
docker run -d --name mycontainer -p 8000:8000 statimage
```

## Описание проекта

Сбор данных происходит при помощи post запроса на эндпоинт:

```
/data/
```

формат входных данных:

```
{
    "device_id": 1, - Идентификатор устройства, c которого происходит сбор
    "x": 100,
    "y": 200,
    "z": 300
}
```

Для создания устройства необходимо отправить post запроса на эндпоинт:

```
/device/
```

Если пользователь авторизован в системе, его id автоматически к созданному устройству

Более подробное описание проекта доступно при запросе к эндпоинту:

```
/docs/
```

## Результаты нагрузочного тестирования

![Результаты нагрузочного тестирования](/images/test.jpg)


## Автор:

- [Скрябина Ольга](https://github.com/ibonish)
