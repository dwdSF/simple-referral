# simple-referral
Реферальная система с авторизацией по номеру телефона


## Инструкция по запуску
  - Склонировать репозиторий к себе на компьютер
  - Установить виртуальное окружение и активировать
```shell
python3 -m venv env
source env\bin\activate
```
  - Установить зависимости
```shell
pip3 install -r requirements.txt
```
  - Установить PostgreSQL и ввести свои данные бд в настройках приложения
```shell
'NAME': '...',
'USER': '...',
'PASSWORD': '...',
```
  - Выполнить миграции
```shell
python3 manage.py makemigrations
python3 manage.py migrate
```
  - Создать пользователя для доступа к админке
```shell
python3 manage.py createsuperuser
```
  - Запуск web-приложения
```
python3 manage.py runserver
```
  
 ## Опционально:
   - Чтобы использовать Twilio для отправки SMS-кода
```shell
1. В /accounts/utils.py/ ввести свои данные от сервиса
2. Раскомментировать вызов функции send_sms() в /accounts/views.py/
```
   - Тестами покрыты основные функции и действия пользователей
```shell
./manage.py test          - запуск всех тестов
./manage.py test accounts - тестирование логина и верификации
./manage.py test codes    - тестирование логики кодов
./manage.py test referral - тестирование работы профилей
```
