#codigo creado por: Alexander Pinchao 
#fecha: 10 de junio del 2016
#importamos el paquete de expresiones regulares 
import re
#abrimos el archivo de texto con los valores de coordenadas del boundongbox  y la fecha
file=open("compendio.txt")
#asignamos el texto del archivo a una variable
texto=file.read()
#cerramos el archivo 
file.close()
#creamos la expresion regular para capturar el dia y la hora asi como las coordenadas del boundingbox 
patron=re.compile(ur'(\D*\s+\D+\s+\d+\s+\d+:\d+:\d+\s\D\d+\s\d+),\s(\D\d+\D\d+),(\D\d+\D\d+),(\D*\d+\D\d+),(\D*\d+\D\d+),(\D*\d+\D\d+),(\D*\d+\D\d+),(\D*\d+\D\d+),(\D*\d+\D\d+)\s')
#damos el formato al texto de la variable
text='u'+texto
#comparamos el texto de la variable con el patron 
m=re.findall(patron,text)
#recorremos la tupla creada 
for x in m:
   #asignamos el valor del elemento de la tupla a una variable 
   lat1=float(str(x[3]))
   #asignamos el valor del elemento de la tupla a una variable 
   lat2=float(str(x[5]))
   #comparamos los valores y deteminamos el orden de operacion  
   if(lat1>lat2):
      #operamos los valores para obtener un solo valor unificado de latitud
    lattot=lat2+(lat1-lat2)/2
    #operamos el caso escepcion de los valores de latitud
   else:
      #operamos los valores para obtener un solo valor unificado de latitud
    lattot=lat1-(lat1-lat2)/2
    #asignamos el valor del elemento de la tupla a una variable 
   lon1=float(str(x[2]))
   #asignamos el valor del elemento de la tupla a una variable 
   lon2=float(str(x[4]))
    #comparamos los valores y deteminamos el orden de operacion  
   if(lon1>lon2):
       #operamos los valores para obtener un solo valor unificado de longitud
    lontot=lon2+(lon1-lon2)/2
   else:
       #operamos los valores para obtener un solo valor unificado de latitud con el caso complementario
    lontot=lon1-(lon1-lon2)/2
    #imprimimos los valores de fecha y magnitudes en consola
   print str(x[0])+","+str(lattot)+","+str(lontot)
    #los valores se imprimiran en consola en caso de desear un archivo de texto usar el modificador >>nomnbreArchivo.txt 
  #escrito a continuacion de la orden de compilacion ejemplo (~#pyhton archi.py>>archivo.txt)
 
