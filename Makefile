
all:
	docker-compose up

build:
	docker-compose build

django-startproject:
	docker-compose run web django-admin.py startproject proyecto .
	sudo chown -R $USER:$USER .

django-create-app:
	docker-compose run web python manage.py startapp $(NAME)

import-data:
	docker-compose exec mongo mongoimport --db movies --collection pelis --file /archivos/datos/movies.json

install:
	# install docker
	sudo apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common -y
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
	sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
	sudo apt-get update
	sudo apt-get install docker-ce

	# install docker compose
	sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
	sudo chmod +x /usr/local/bin/docker-compose
