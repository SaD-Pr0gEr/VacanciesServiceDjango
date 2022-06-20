# Vacancies service Python(analogue [hh.ru](https://hh.ru))
Website for find vacancies and response them

## Project Installation
1. Clone
```
git clone https://github.com/SaD-Pr0gEr/VacanciesServiceDjango.git
```
2. Install requirements
```
pip3 install -r requirements/dev.txt
for prod
pip3 install -r requirements/prod.txt
```
3. run dev server
``` 
python3 manage.py runserver --settings=vacansies_service.settings.dev
for production
python3 manage.py runserver --settings=vacansies_service.settings.prod
```
## Docker
1. Build
``` 
docker-compose build
```
2. Run
``` 
docker-compose up
```
