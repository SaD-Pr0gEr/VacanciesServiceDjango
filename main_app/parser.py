# import os
# import sys
# import time
# from pathlib import Path
# from uuid import uuid4
# import requests
# from bs4 import BeautifulSoup
#
# project_path = Path(__file__).resolve().parent.parent
# sys.path.append(project_path)
# os.environ['DJANGO_SETTINGS_MODULE'] = f'{project_path.name}.settings.dev'
#
# import django
# django.setup()
#
# from main_app.models import Vacancy, Cities, ProgramLanguage
#
# __all__ = (
#     'runner_work_ua',
#     'geek_job_links',
#     'parser_geek_job',
# )
#
#
# def language_checker(languages, str_language):
#     """Функция проверки языка в БД"""
#
#     language = None
#     for get_language in languages:
#         if str(get_language.name.lower()) == str_language.lower():
#             return get_language
#     if not language:
#         language = ProgramLanguage.objects.create(name=str_language, slug=uuid4())
#         return language
#
#
# def city_checker(cities, str_city):
#     """Функция проверки города в БД"""
#
#     city = None
#     for get_city in cities:
#         if str(get_city.name.lower()) == str_city.lower():
#             return get_city
#     if not city:
#         city = Cities.objects.create(name=str_city.lower(), slug=uuid4())
#         return city
#
#
# def get_response(url, headers):
#     """Функция отправки запроса"""
#
#     response = requests.get(url, headers=headers)
#     if int(response.status_code) != 200:
#         return None
#     return response
#
#
# def convert_soup(response):
#     """Функция для конвертирования в soup"""
#
#     soup = BeautifulSoup(response.text, 'html.parser')
#     return soup
#
#
# def parse_work_ua(soup):
#     """Функция парсинга сайта work.ua"""
#
#     job_card_container = soup.find('div', attrs={'id': 'pjax-job-list'})
#     cities_list = Cities.objects.all()
#     language_list = ProgramLanguage.objects.all()
#     if job_card_container:
#         job_cards = job_card_container.find_all('div', attrs={"class": "job-link"})
#         if job_cards:
#             city_list = []
#             cities = soup.find('div', attrs={"id": "city-seo-block"}).find('ul').find_all('li')
#             if cities:
#                 for city in cities:
#                     city_list.append(city.a.text.lower())
#             language = soup.find("h1", attrs={"class": 'text-basic'}).text.split(" ")[0].split('\n')[0]
#             if language:
#                 new_language = language_checker(language_list, language)
#                 for card in job_cards:
#                     card_dict = {}
#                     job_title = card.select('h2 > a')[0]
#                     name = job_title.text
#                     url = f"https://www.work.ua{job_title['href']}"
#                     company = card.select('.add-top-xs > span > b')[0].text
#                     description = card.p.text.replace('\n', ' ').replace('\u2060', ' ').replace("\xa0", ' ').replace("                           ", ' ').strip()
#                     job_card = card.find('div', attrs={'class': "add-top-xs"}).find_all('span')
#                     city = ''
#                     for get_city in job_card:
#                         check_city = get_city.text.lower()
#                         if check_city in city_list:
#                             city = check_city
#                     new_city = city_checker(cities_list, city)
#                     card_dict['name'] = name
#                     card_dict['url'] = url
#                     card_dict['company'] = company
#                     card_dict['description'] = description
#                     card_dict['city'] = new_city
#                     card_dict['language'] = new_language
#                     try:
#                         Vacancy.objects.create(**card_dict)
#                     except Exception as e:
#                         print(e)
#                         continue
#                 return True
#
#
# def runner_work_ua(languages_list, headers):
#     """Функция движок для запуска парсера для сайта work.ua"""
#
#     base_url_work_ua = 'https://www.work.ua/ru'
#     for lang in languages_list:
#         link_work_ua = f"{base_url_work_ua}/jobs-{lang}"
#         res = get_response(link_work_ua, headers)
#         if res:
#             res_soup = convert_soup(res)
#             parse_work_ua(res_soup)
#             time.sleep(2)
#
#
# def parser_geek_job(link_list: list, headers):
#     """Функция для парсинга сайта geekjob.ru"""
#
#     ready_data = []
#     cities = Cities.objects.all()
#     for link in link_list:
#         response = get_response(link['link'], headers)
#         if response:
#             soup = convert_soup(response)
#             work_header = soup.select('section.col > header')
#             if work_header:
#                 work_header = soup.select('section.col > header')[0]
#                 name = work_header.h1.text
#                 company = work_header.find('h5', attrs={'class': 'company-name'}).find('a').text
#                 description_container = soup.find('div', attrs={'id': 'vacancy-description'}).find_all('p')
#                 description = ''
#                 for text in description_container:
#                     description += text.text
#                 str_city = work_header.find('div', attrs={'class': "location"}).text.split(',')[0].lower()
#                 if len(str_city) == 1:
#                     city = city_checker(cities, str_city)
#                 else:
#                     city = None
#                 language = link['language']
#                 add_data = {
#                     "url": link['link'],
#                     "name": name,
#                     "company": company,
#                     "description": description,
#                     "city": city,
#                     'language': language
#                 }
#                 try:
#                     Vacancy.objects.create(**add_data)
#                 except Exception as e:
#                     print(e)
#                     continue
#         time.sleep(2)
#     return ready_data
#
#
# def geek_job_links(language_list, headers):
#     """Функция для получение ссылок на страницу с вакансий сайта geekjob.ru"""
#
#     base_url = 'https://geekjob.ru/json/find/vacancy'
#     links_list = []
#     for language in language_list:
#         link = f'{base_url}?page=1&qs={language}'
#         response = get_response(link, headers)
#         if response:
#             json_data = response.json()['data']
#             for data in json_data:
#                 link_id = data['id']
#                 work_link = f'https://geekjob.ru/vacancy/{link_id}'
#                 links_list.append({"link": work_link, 'language': language})
#         time.sleep(2)
#     return links_list
