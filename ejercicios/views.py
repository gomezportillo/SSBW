from django.shortcuts import render
from django.shortcuts import HttpResponse, render

from random import randint
import os
import re
import requests

from pymongo import MongoClient
from bson import ObjectId

# Configuring the logger
import logging
logger = logging.getLogger(__name__)


# Configuring MongoDB
client = MongoClient('mongo', 27017)
db = client.movies
pelis = db.pelis


"""
Tema 1
"""
def ejercicio_1_1(request, usuario):
	"""
	Salute the user
	"""

	msg = """
		<html>
   		<h2>
  			Hola {}. Cómo estás?
		</h2>
		</html>""".format(usuario)

	logger.info('The user has been just saluted!')
	return HttpResponse(msg)


def ejercicio_1_2(request, usuario):
	"""
	SALUTE THE USER!!
	"""
	msg = """
		<html>
   		<h2>
  			Hola {}! Cómo estás crack?
		</h2>
		</html>""".format(usuario.upper())

	return HttpResponse(msg)


def ejercicio_1_3(request, year):
	"""
	Send your best regards to the new year
	"""
	if year == 2019:
		msg = 'Feliz año!'
	else:
		msg = 'Te has equivocado de año...'

	out = """HttpResponse
		<html>
   		<h2>{}</h2>
		</html>""".format(msg)

	return HttpResponse(out)


"""
Tema 2
"""

def ejercicio_2_1(request, lista):
	str_array = lista.split(' ')

	counter = 0
	for str1 in str_array:
		if len(str1) >= 2:
			counter += 1

	response = "<h2>Number of strings whose length is =>2: {}</h2>".format(counter)

	counter = 0
	for str1 in str_array:
		for str2 in str_array:
			if str1 != str2:
				if str1[0] == str2[0] and str1[-1] == str2[-1]:
					counter += 1

	response += "<h2>Number of string whose first and last char are the same: {}</h2>".format(counter)

	return HttpResponse(response)


def ejercicio_2_2(request, lista):
	str_array = lista.split(' ')
	str_set = set(str_array)

	response = '<h2>{}</h2>'.format(str_set)

	return HttpResponse(response)


def ejercicio_2_3(request, s):
	if len(s) < 2:
		result = ""
	else:
		result = s[:2] + s[-2:]

	response = '<h2>{}</h2>'.format(result)
	return HttpResponse(response)


def ejercicio_2_4(request, s):
	if len(s) >= 3:
		if s[-3:] != 'ing':
			end = 'ing'
		else:
			end = 'ly'
	else:
		end = None

	response = '<h2>{}</h2>'.format(s + end)
	return HttpResponse(response)


def ejercicio_2_5(request):
	text = """"
	Read any text file specified on the command line. Do a simple split() on
	whitespace to obtain all the words in the file. Rather than read the file
	line by line, it's easier to read it into one giant string and split it once.

	Build a "mimic" dict that maps each word that appears in the file to a list
	of all the words that immediately follow that word in the file. The list of
	words can be be in any order and should include duplicates. So for example
	the key "and" might have the list ["then", "best", "then", "after", ...]
	listing all the words which came after "and" in the text. We'll say that the
	empty string is what comes before the first word in the file.

	With the mimic dict, it's fairly easy to emit random text that mimics the
	original. Print a word, then look up what words might come next and pick one
	at random as the next work. Use the empty string as the first word to prime
	things. If we ever get stuck with a word that is not in the dict, go back to
	the empty string to keep things moving.

	Note: the standard python module 'random' includes a random.choice(list)
	method which picks a random element from a non-empty list.

	For fun, feed your program to itself as input. Could work on getting it to
	put in linebreaks around 70 columns, so the output looks better.
	"""

	signs = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

	clean_text = text.lower()
	for sign in signs:
		clean_text = clean_text.replace(sign, '')

	clean_text = clean_text.split()

	dict = {}
	total_lenght = len(clean_text)

	for index, word in enumerate(clean_text):
		if index < total_lenght-1:	# if the for has not reached the end of the list
			if word not in dict:
				dict[word] = []

			dict[word].append( clean_text[index+1] ) # appending the next word to it

	final_text = ""		# generate the final text randomly
	for word in dict:
		final_text += word + " " + pick_word_at_random(dict[word]) + " "

	response = '<h2>{}</h2>'.format(final_text)
	return HttpResponse(response)


def pick_word_at_random(list):
	lenght = len(list)
	index = randint(0, lenght - 1)
	return list[index]

"""
Tema 3
"""
# https://regex101.com/
def ejercicio_3(request):

	URL = 'http://ep00.epimg.net/rss/tags/ultimas_noticias.xml'
	REGEX = r"<item>\W+<title><\!\[CDATA\[(.+?)\]\]><\/title>"
	titulares = []

	req = requests.get(URL)
	if req.status_code == 200:

		match = re.findall(REGEX, req.text)

		for item in match:
			titulares.append({'title': item})


	context = {
		'newspaper' : 'El País',
		'titulares': titulares
	}

	return render(request, 'ejercicio_3.html', context)


"""
Tema 4
"""
def ejercicio_4(request, my_limit):

	pelis_list = pelis.find(limit=my_limit)


	context = {
		'limit': my_limit,
		'pelis': pelis_list
	}
	# return HttpResponse(pelis_list)
	return render(request, 'ejercicio_4.html', context)


"""
Tema 5
"""
def ejercicio_5_actor(request, actor):

	regex = re.compile(actor, re.IGNORECASE)
	pelis_list = pelis.find({'actors':regex})

	context = {
		'busqueda': actor,
		'pelis': pelis_list
	}
	return render(request, 'ejercicio_5_resultado.html', context)


# Actualizacion tema 9: Limitar el numero de pelis que devuelve en funcion de si el usuario está autentificado
def ejercicio_5_title(request, title):
	MAX_PELIS = 5

	regex = re.compile(title, re.IGNORECASE)

	if request.user.is_authenticated:
		pelis_list = pelis.find({'title':regex})
	else:
		pelis_list = pelis.find({'title':regex}).limit(MAX_PELIS)


	context = {
		'busqueda': title,
		'pelis': pelis_list
	}
	return render(request, 'ejercicio_5_resultado.html', context)


def ejercicio_5_buscar(request):
	if request.GET.get('actor'):
		return ejercicio_5_actor(request, request.GET.get('actor'))

	elif request.GET.get('title'):
		return ejercicio_5_title(request, request.GET.get('title'))

	else:

		movies_list = ""
		for peli in pelis.find():
			movies_list += "\"{}\",\n".format(peli['title'])

		context = {
			'movies_list': movies_list[:-2] # removing last comma
		}

		return render(request, 'ejercicio_5_buscar.html', context)


"""
Tema 6
"""
def ejercicio_6(request, id):
	peli = pelis.find_one({'_id': ObjectId(id)})

	# Fix image URL
	if peli['poster']:
		peli['poster'] = peli['poster'].replace('http://ia.media-imdb.com', 'https://m.media-amazon.com')

	context = {
		'peli' : peli
	}

	return render(request, 'ejercicio_6_info.html', context)


"""
Tema 7
"""
from django import forms
from django.http import HttpResponseNotAllowed

class EditForm(forms.Form):

	_id 	 = forms.CharField(max_length=999)
	title 	 = forms.CharField(max_length=999)
	year 	 = forms.IntegerField()
	runtime  = forms.IntegerField()
	director = forms.CharField(max_length=999)
	poster   = forms.CharField(max_length=999)
	plot 	 = forms.CharField(widget=forms.Textarea)


def ejercicio_7_edit(request, id):

	if request.method == 'POST':
		form = EditForm(request.POST)

		if form.is_valid():
			updated_movie = request.POST
			criteria = {'_id': ObjectId(updated_movie['_id'])}
			changes = {"$set" : {'title' : updated_movie['title'],
								 'year' : updated_movie['year'],
								 'runtime' : updated_movie['runtime'],
								 'director' : updated_movie['director'],
								 'poster' : updated_movie['poster'],
								 'plot' : updated_movie['plot']}}
			pelis.update_one(criteria, changes)

			return HttpResponse('Película actualizada correctamente!✔️')

	else:
		peli = pelis.find_one({'_id': ObjectId(id)})
		form = EditForm(initial=peli)

	return render(request, 'ejercicio_7_edit.html', {'form': form})


from django.views.decorators.csrf import csrf_exempt

# Ha sido implsible hacer mandar la token CSRF desde javascript asique lo deshabilito
# La linea que borra películas ha sido comentada
@csrf_exempt
def ejercicio_7_delete(request, id):
	if request.method == 'DELETE':
		peli = pelis.find_one({'_id': ObjectId(id)})
		if (peli):
			criteria = {'_id' : id}
			# pelis.delete_one(criteria)
			print("Peli " + peli['title'] + " borrada correctamente✔️")

			return HttpResponse('Película borrada correctamente!✔️')

	else:
		return HttpResponseNotAllowed('Solamente está permitida la petición HTTP DELETE en esta ruta')


@csrf_exempt
def ejercicio_11_like(request, id):
	if request.method == 'POST':
		print("LIKED movie " + id)
		return HttpResponse(randint(1, 99))
