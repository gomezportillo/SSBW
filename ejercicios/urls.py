from django.urls import path

from . import views

from django.conf.urls import include, url
from rest_framework import routers
from .viewsets import PelisViewSet

router = routers.DefaultRouter()
router.register('pelis', PelisViewSet, 'peli')

urlpatterns = [

	# Tema 1: Python 101
	path('1/1/<str:usuario>', views.ejercicio_1_1),
	path('1/2/<str:usuario>', views.ejercicio_1_2),
	path('1/3/<int:year>', views.ejercicio_1_3),

	# Tema 2: Python exercises
	path('2/1/<str:lista>', views.ejercicio_2_1), # lista separada por espacio
	path('2/2/<str:lista>', views.ejercicio_2_2), # lista separada por espacio
	path('2/3/<str:s>', views.ejercicio_2_3), # un string
	path('2/4/<str:s>', views.ejercicio_2_4), # un string
	path('2/5', views.ejercicio_2_5), # da igual

	# Tema 3: Django Templates, Jinja, requests, RSS feeds and regular expresions
	path('3', views.ejercicio_3),

	# Tema 4. MongoDB
	path('4/<int:my_limit>', views.ejercicio_4),

	# Tema 5. Responsive CSS frameworks
	path('pelis', views.ejercicio_5_buscar, name='pelis'),
	# path('pelis/actor/<str:actor>', views.ejercicio_5_resultado),

	# Tema 6. CSS
	path('pelis/info/<str:id>', views.ejercicio_6, name='info'),

	# Tema 7. CRUD
	path('pelis/edit/<str:id>', views.ejercicio_7_edit, name='edit'),
	path('pelis/delete/<str:id>', views.ejercicio_7_delete, name='delete'),

	# Tema 11. AJAX
	path('pelis/like/<str:id>', views.ejercicio_11_like, name='like'),

	# Tema 12. API REST
	path('api_pelis',    views.api_pelis),  # GET lista todas, POST añade
	path('api_peli/<id>', views.api_peli),  # GET lista una,   PUT modifica, DELETE borrra

	url('api', include(router.urls)), # Incluye todo el API CRUD
]
