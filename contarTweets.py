#codigo creado por: Luis Sosa 
#fecha: 10 de junio del 2016
#archivo creado para contar el numero de tweets en un archivo json
import re
#abrimos el archivo json 
file=open("pichincha.json")
#asignamos los datos encontrados en una variable 
texto=file.read()
#cerramos el archivo
file.close()
#creamos la expresion regular que nos permitira saber el numero de tweets en el archivo 
patron = re.compile(ur'created_at":([^,]+),"f[^j]*[^\[]+([^}]+)')
#damos formato al texto 
text='u'+texto
#comparamos los datos de la variable con la expresion regular y lo agregamos a una tupla
m=re.findall(patron,texto)
#imprime el valor de la longitud de la tupla 
print len(m)

