from mongoengine import *

connect('movies', host='mongo')

class Pelis(Document):
	title     = StringField(required=True)
	year      = IntField(min_value=1900)
	rated     = StringField()
	runtime   = IntField()
	countries = ListField(StringField())
