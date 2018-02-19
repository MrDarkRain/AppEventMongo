from django.shortcuts import render
from django.http import HttpResponse
#import mongoengine
#from mongoengine import authenticate
# Create your views here.


#user = authenticate(username=username, password=password)
#assert isinstance(user, mongoengine.django.auth.User)

from pymongo import MongoClient
 

def index_eventos(request):
	
	client = MongoClient('mongodb://Proyectosw2:Proyectosw2@ds235708.mlab.com:35708/rusia2018sw2')

	db = client['rusia2018sw2']
 
	person1 = { "name" : "Arturo", "age" : 25, "dept": 101, "languages":["English","German","Japanese"] }
 
	person2 = { "name" : "Jane Doe", "age" : 27, "languages":["English","Spanish","French"] }


	print ("clearing")
	db.employees.remove()

 
	print ("guardando")
	db.employees.save(person1)
	db.employees.save(person2)
 
	print ("searching")
	for e in db.employees.find():
		print (e["name"])


	return HttpResponse("<h1>Soy la pagina principal</h1>")
