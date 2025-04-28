# Учебный проект 

данный репозиторий является моим учебным проектом представляет собой 
сайт питомник собак в этом проекте я скорее знакомлюсь джанго и его возможностями
пробую себя 



Проект включает в себя следующие разделы:
- породы 
- собаки 
- пользователи
- отзывы
далее опишу его как настроить
 Виртуальное окружение для проекта: venv
## Предварительные условия
В вашей системе должны быть установлены
- Python (версия 3.6 или выше) и pip.
- Установлен фреймворк Django (версии 3.2 или выше).
- Установлен redis 

## Установка

1.  Настройте свое виртуальное окружение и установите зависимости из файла requirements.txt

```bash
pip install -r requirements.txt
```

2. Клонируйте репозиторий на свой локальный компьютер:
```
git clone https://github.com/your-username/cbv_django
```

3. создайте и заполните .env file согласно .env_sample
```
pip install -r requirements.txt
```
4. Создайте базу данных при помощи команды 
```  bash
python manage.py ccdb
```
5. Добавить и провести миграции:
```
python manage.py makemigrations
python manage.py migrate
```
5. Выполните команду для создания пользователей
```bash
python manage.py ccsu
```
6. Выполните команду для заполнения базы данных используя фикстуры
```bash
python -Xutf8 manage.py loaddata  backup/dogs.json     
python -Xutf8 manage.py loaddata  backup/users.json     
python -Xutf8 manage.py loaddata  backup/reviews.json   


```

## Для запуска приложения
если вы выполнили предыдущие пункты  все должно сработать успешно
```bash
redis-server 
python manage.py runserver
```
### Дополнительно
доступны команды 
ссdb - для создания базы
ссsu - Для пользователей user moderaror admin
test_mail - для проверки отправки писем 
находятся в приложение users managment

