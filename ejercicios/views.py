from django.shortcuts import render
from django.shortcuts import HttpResponse

def ejercicio_1(request, usuario):

	msg = """
		<html>
   		<h2>
  			Hola {}! Cómo estás crack?
		</h2>
		</html>""".format(usuario)

	return HttpResponse(msg)


def ejercicio_2(request, usuario):
	msg = """
		<html>
   		<h2>
  			Hola {}! Cómo estás crack?
		</h2>
		</html>""".format(usuario.upper())

	return HttpResponse(msg)

def ejercicio_3(request, year):
	if year == 2019:
		msg = 'Feliz año!'
	else:
		msg = 'Te has equivocado de año...'
	
	out = """
		<html>
   		<h2>{}</h2>
		</html>""".format(msg)

	return HttpResponse(out)
