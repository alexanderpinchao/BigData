#codigo creado por: Montufar Diego
#agreagmos el paquete de expresiones regulares
import re
#agregamos el paquete para manejar couchdb
import couchdb
#agregamos los paquetes de tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
#Agregamos el paquete para manejar objetos json
import json


###API ########################
#Credenciales de acceso a twitter
ckey = "nZPXeBQmpn7lVh3k7RhfqdX9K"
csecret = "uOsWTomsSntwHAz9vkXLcTASdmaW6yykWoxDQGSyT4yttlBLrx"
atoken = "731096320363114496-cWWceoZ0OpeaMPHYanzDSFLi4FDIWgW"
asecret = "ENS0HkrqCrhaFZX56AJloTYFigsvmNCyBQxk83szFaPmo"
#####################################
#creacion del listener
class listener(StreamListener):
#obtenemos la informacion de la API conserniente al tweet
    def on_data(self, data):
    	#agregamos esta informacion a un objeto json
        dictTweet = json.loads(data)
        #creamos un bloque de control para comprobar si el tweet ya existe o no
        try:
        	#agregamos la id al objeto a ingresar
            dictTweet["_id"] = str(dictTweet['id'])
#generacion de la expresion regular con el termino a buscar 
            p=re.compile(ur'"Quito"')
#copia el texto del mesaje de twitter dentro de una variable y la prepara para ser prosesada
            buscar='u'+data
#compara la expresion regular y el texto y asigna el valor obtenido a una lista
            m=re.findall(p,buscar)
#compara la longitud de la lista si es cero el termino jamas aparecio y en caso de ser
#mayos a cero el termino esta presente en el texto
	    if(len(m)==0):
#en caso de que el termino aparesca en el texto agrega el documento en la base de datos 
            else:
#en caso de que el termino aparesca en el texto agrega el documento en la base de datos 
               doc = db.save(dictTweet)
        except:
        	#en caso de existir el tweet imprimimos un mensaje 
            print "Already exists"
            pass
           #cambiamos el valor de la bandera a verdadero
        return True
    
    def on_error(self, status):
        print status
        #agregamos los valores a nuestro listener para su consumo 
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('quito')
except:
    db = server['quito']
    
'''===============LOCATIONS=============='''    
#definimos el boundingbox para filtrar la informacion obtenida desde twitter
twitterStream.filter(locations=[-78.519888,-0.149774,-78.422213,-0.100164])  #Quito
