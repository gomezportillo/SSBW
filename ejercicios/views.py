from django.shortcuts import render
from django.shortcuts import HttpResponse, render

from random import randint
import os
import re
import requests

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

	out = """
		<html>
   		<h2>{}</h2>
		</html>""".format(msg)

	return HttpResponse(out)


"""
Tema 2
"""

def ejercicio_2_1(request, lista):
	"""
	Given a list of strings, return the count of the number of strings where the
	string length is 2 or more and the first and last chars of the string are
	the same.
	"""
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
	"""
	Given a list of numbers, return a list where all adjacent == elements have
	been reduced to a single element, so [1, 2, 2, 3] returns [1, 2, 3]. You may
	create a new list or modify the passed in list.
	"""
	str_array = lista.split(' ')
	str_set = set(str_array)

	response = '<h2>{}</h2>'.format(str_set)

	return HttpResponse(response)


def ejercicio_2_3(request, s):
	"""
	Given a string s, return a string made of the first 2 and the last 2 chars
	of the original string, so 'spring' yields 'spng'. However, if the string
	length is less than 2, return instead the empty string.
	"""

	if len(s) < 2:
		result = ""
	else:
		result = s[:2] + s[-2:]

	response = '<h2>{}</h2>'.format(result)
	return HttpResponse(response)


def ejercicio_2_4(request, s):
	"""
	Given a string, if its length is at least 3, add 'ing' to its end. Unless it
	already ends in 'ing', in which case add 'ly' instead. If the string length
	is less than 3, leave it unchanged.
	"""
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
