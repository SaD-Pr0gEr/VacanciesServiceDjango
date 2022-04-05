# Сервис вакансий Python(Аналог сайта [hh.ru](https://hh.ru))
Сайт для опубликования вакансий, отклика на вакансий и тп... Просто скачайте и 
запускайте. Пример ```.env``` файла есть на репозиторий

## Установка и первый запуск
1. Клонируем репозиторий 
```
git clone https://github.com/SaD-Pr0gEr/VacanciesServiceDjango.git
```
2. Установим зависимости
```
pip3 install -r requirements/dev.txt
```
3. Запускаем dev сервер
``` 
python3 manage.py runserver --settings=vacansies_service.settings.dev
или c production настройками
python3 manage.py runserver --settings=vacansies_service.settings.prod
```
## Работа с docker
1. Соберём контейнеры
``` 
docker-compose build
```
2. Запускаем
``` 
docker-compose up
```
