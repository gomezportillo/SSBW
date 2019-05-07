# AJAX, ES6 fetch

En esta tarea vamos a añadir un nuevo campo númerico a cada peli, que aumente o disminulla 'me gusta' o 'no me gusta'.

Pondremos iconos , y , podemos usar [Font Awesone](https://fontawesome.bootstrapcheatsheets.com/), o los que sugiere [Boostrap](https://getbootstrap.com/docs/4.0/extend/icons/).

Los botones haran una llamada al servidor, que responderá con el valor correspodiente para insertarlo en la página.

Para la comunicación asíncrona con el servidor, podemos usar [AJAX de jQuery](http://librosweb.es/libro/fundamentos_jquery/capitulo_7/metodos_ajax_de_jquery.html), o bien [fetch de ES6](https://developer.mozilla.org/es/docs/Web/API/Fetch_API/Utilizando_Fetch). Si usamos una petición POST o PUT al servidor, que sería lo lógico puesto que vamos a modificar la Base de Datos, tenemos que incluir el token [csrf de Django](https://stackoverflow.com/questions/8614947/jquery-and-django-csrf-token). Ver [Using the Fetch Api with Django Rest Framework](https://gist.github.com/marteinn/3785ff3c1a3745ae955c).

El valor que se envie del servidor lo podemos volover a poner en su sitio con el método [html](http://api.jquery.com/html/) de jQuery.
