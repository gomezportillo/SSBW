from django.urls import path

from . import views

urlpatterns = [
	path('1/<str:usuario>', views.ejercicio_1),
	path('2/<str:usuario>', views.ejercicio_2),
	path('3/<int:year>', views.ejercicio_3),
	# path('3/<int:year>/<int:month>', views.ejercicio_3),
	# path('4/<slug:slug>', views.ejercicio_4),
]
