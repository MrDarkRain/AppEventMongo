from django.shortcuts import render
from django.http import HttpResponse
#import mongoengine
#from mongoengine import authenticate
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

import simplejson as json
import json as json2
from bson import ObjectId
from bson.son import SON


from pymongo import MongoClient


client = MongoClient('mongodb://Proyectosw2:Proyectosw2@ds235708.mlab.com:35708/rusia2018sw2')
db = client['rusia2018sw2']

def index(request):
	#return render(request, 'graficos/graficoBarra.html')
    return render(request, 'index.html')

def index_eventos(request):

	

	

	person1 = { "name" : "Arturo", "age" : 25, "dept": 101, "languages":["English","German","Japanese"] }

	person2 = { "name" : "Jane Doe", "age" : 27, "languages":["English","Spanish","French"] }


	print ("clearing")
	#db.eventos.remove()


	print ("guardando")
	db.eventos.save(person1)
	db.eventos.save(person2)

	print ("searching")
	for e in db.eventos.find():
		print (e["name"])


	return HttpResponse("<h1>Soy la pagina principal</h1>")


def evento_grafico(request):

    return render(request, 'graficos/graficoBarra.html')


@csrf_exempt
def validar(request):
	print("entro a validar")
	if request.method == 'POST':
		infopost = request.POST.__getitem__('data')
		evento = json.loads(infopost)

		print(evento)
		print(evento['usuario'])
		print(evento['tipoevento'])
		#print(evento['fecha'])

		print ("clearing")
		#db.eventos.remove()


		print ("guardando")
		db.eventos.save(evento)


		temp = { 'rpta' : 'true' }	
		data_string = json.dumps(temp)
	
	else:
		print("algo va mal")
	return HttpResponse(data_string, content_type='application/json')

@csrf_exempt
def mostrarinfo(request):

	data = db.eventos.find()
	
	"""
	lst_eventos = []
	for e in data:
		lst_eventos.append(e)
		#print (e["usuario"])
		#print (e["dia"])
	temp = {
		'collection' : lst_eventos
	}
	

	json_report = JSONEncoder().encode(temp)
	"""
	#print(lst_eventos)
	listaeventos = []
	cont = 0;
	for i in data:
		cont = cont + 1;
		event = {'id': cont,
				'usuario':i['usuario'],
				'tipoevento':i['tipoevento'],
				'hora':i['hora'],
				'minuto':i['minuto'],
				'dia':i['dia'],
				'mes':i['mes'],
				'año':i['año'],
				'diasemana':i['diasemana']
		}
		listaeventos.append(event)
	listajson = json.dumps(listaeventos)

	return HttpResponse(listajson, content_type='application/json')

class JSONEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, ObjectId):
			return str(o)
		return json2.JSONEncoder.default(self, o)


