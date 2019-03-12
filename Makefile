
all:
	docker-compose up

build-docker:
	docker-compose build

django-startproject:
	docker-compose run web django-admin.py startproject proyecto .
	sudo chown -R $USER:$USER .

django-create-app:
	docker-compose run web python manage.py startapp $(NAME)

build:
	docker-compose build

import-data:
	docker-compose exec mongo mongoimport --db movies --collection pelis --file /archivos/datos/movies.json
