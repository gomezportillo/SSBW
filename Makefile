
all:
	docker-compose up

django-startproject:
	docker-compose run web django-admin.py startproject proyecto .
	sudo chown -R $USER:$USER .
	
