#agregamos el paquete de expresiones regulares 
import re
#agregamos el paquete de manejo para couchdb
import couchdb
#agregamos el paquete de manejo de json
import json
#abrimos el archivo de texto con la informacion obtenida del archivo que unificarCoordenadas.py
file =open("latlon.txt")
#leemos el archivo y asignamos los datos a una variable
texto=file.read()
#cerramos el archivo 
file.close()
#nos conectamos a nuestra base de datos 
server = couchdb.Server('http://localhost:5984/')
#abrimos un bloque de comprobacion para comprobar la existencia de nuestra base de datos 
try:
    #en caso de no existir la creamos 
    db = server.create('coordenadas')
except:
    #en cso de existir la conectamos 
    db = server['coordenadas']
    #creamos un patron para separa los datos de fecha por Dia, Hora y los valores de las coordenads
patron=re.compile(ur'\s(\D{3})\s\D+\s\d+\s(\d+):\d+:[^,]+,([^,]+),(\D\d\D\d+)')
#comprobamos el patron en los datos 
m=re.findall(patron,texto)
#recorremos las tupla de resultado
for x in m:
    #damos el formato json a la informacion 
  ingreso='{"dia":"'+str(x[0])+'","hora":"'+str(int(x[1]))+'","coordenadas": {"latitud": '+str(x[3])+',"logitud": '+str(x[2])+'}}'
  #cargamos en un objeto json los datos con formato
  ingres_json=json.loads(ingreso)
  #el objeto json a la base de datos 
  doc=db.save(ingres_json)
  
  #Advertencia este proceso puede ser extremadamente largo en terminar 246316 registros como el creado en este ejercicio demoraron 210 minutos
  
  
