# Autorización CRUD

En esta tarea completaremos el CRUD añadiendo autorización, de manera que solo los usuarios que sean 'staff' puedan añdir, borrar o modificar registos. En [Tutorial de Django Parte 8: Autenticación y permisos de Usuario](https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Authentication) viene un ejemplo bastante detallado.

Referencias:
[User model](https://docs.djangoproject.com/en/2.2/ref/contrib/auth/)


## Notas

Nosotros haremos que si un usuario no está logeado solo pueda obtener una lista de las 5 primeras películas al buscarlas y que si no pertenece al grupo _Staff_ no pueda ni editarlas ni borrarlas.
