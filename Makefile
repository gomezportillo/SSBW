
all:
	docker-compose up

django-startproject:
	docker-compose run web django-admin.py startproject proyecto .
	sudo chown -R $USER:$USER .

django-create-app:
	docker-compose run web python manage.py startapp ejercicios

build:
	docker-compose build
