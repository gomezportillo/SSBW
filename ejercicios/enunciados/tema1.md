# Ejercicios de Python

Prepararemos nuestro entorno de desarrollo para que la entrada y salida de los ejrecicios de python sean a través del navegador. Para esto crearemos una aplicación dentro del proyecto de la tarea anterior:

    $ docker-compose run web python manage.py startapp ejercicios

y la apuntamos en el archivo `proyecto/settings.py`

    ...
    INSTALLED_APPS = (
    	'django.contrib.admin',
    	'django.contrib.auth',
    	'django.contrib.contenttypes',
    	'django.contrib.sessions',
    	'django.contrib.messages',
    	'django.contrib.staticfiles',
    	'ejercicios',
    )
    ...

Prepararemos el [dispatcher](https://docs.djangoproject.com/en/2.2/topics/http/urls/) de nuestro framework para que la entrada y la salida a los ejercicios sea con el navegador. Tendremos que cambiar el enrutador principal `proyecto/urls.py`:

    # proyecto/urls.py

    django.conf.urls import include, url
    django.contrib import admin

    urlpatterns=[
    	url(r'^ejercicicios/',include('ejercicios.urls')),
    	url(r'^admin/',admin.site.urls),
    ]

El encaminamiento de los urls lo ponemos el archivo `ejercicios/urls.py`

    from django.urls import path

    from . import views

    urlpatterns = [
    	path('1/<str:usuario>', views.ejercicio_1),	# entrada str
    	path('2/<int:year>', views.ejercicio_2),	# entrada int
    	path('3/<int:year>/<int:month>', views.ejercicio_3),# dos entradas int
    	path('4/<slug:slug>', views.ejercicio_4),	# entrada slug
    	...
    	]

el código lo pondremos en el archivo `ejercicios/views.py`

    # ejercicios/views.py

    from django.shortcuts import HttpResponse

    def ejercicio_1(request, usuario):

    	salida = '''
    		<html>
       		...
      			Hola %s
    		...
    		</html>''' % (usuario)

    	return HttpResponse(salida)

    ...

De esta manera el url [http://localhost:8000/ejercicios/1/pepe](http://localhost:8000/ejercicios/1/pepe), ejecutará la función `views.ejercicio_1`, etc

Podremos hacer alguno de los ejercicios de [Tutorial interactivo de Python 3 con más de 100 ejercicios](https://snakify.org/es/)
