# API REST

En esta tarea añadiremos una API REST a nuestra aplicación, siguiendo el
[tutorial](http://www.django-rest-framework.org/tutorial/1-serialization/#introduction)
que viene con la docuemenación de [Django Rest
Framework](http://www.django-rest-framework.org) y la adaptación a
mongoengine: [Django + MongoDB = Django REST Framework
Mongoengine](https://medium.com/@vasjaforutube/django-mongodb-django-rest-framework-mongoengine-ee4eb5857b9a).
También [How to setup Django + Django REST Framework + Mongo
?](https://leadwithoutatitle.wordpress.com/2018/03/21/how-to-setup-django-django-rest-framework-mongo/)

Añadimos a **requirements.txt**:

    ...
    djangorestframework
    django-rest-framework-mongoengine

y en el **settings.py**:

    INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_mongoengine'
    ]

Haremos dos versiones del `API`, una donde respondamos desde funciones
en **views.py**, y otra aprovechando el enrutador, y las 'class views'
que incluye el framework.



##### API desde funciones

Seguimos los pasos de la [primera parte del
tutorial](http://www.django-rest-framework.org/tutorial/1-serialization/#introduction)
y creamos lo serializadores, unas clases similares a las de formularios,
que se van a encargar de codificar/decodificar los datos a/desde el
request al model: creamos un archivo **serializers.py**

    # mi_app/serializ
