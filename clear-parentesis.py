#importamos el paquete de expresiones regulares 
import re
#abrimos el archivo con la informacion 
file=open("quito.json")
#asignamos la informacion a una variable para ser utilizada 
texto=file.read()
#cerramos el archivo 
file.close()
#generamos la expresion regular para recolectar las coordenadas y la fecha  
patron = re.compile(ur'created_at":([^,]+),"f[^j]*[^\[]+([^}]+)')
#damos el formato a la variable donde ingrsamos los datos 
text='u'+texto
#procesamos la informacion y asignamos las variables a una tupla de dos columnas con los valores de coordenadas en 
#la primera columna y los de la fecha de creacion en la segunda 
m=re.findall(patron,texto)
#recorremos los valores de la tupla 
for x in m:
  #comvertimos la tupla a una cadena para su procesamiento y la asignamos a una variable 
  key=str(x)	
  #eliminamos los [ de la variable 
  key=key.replace("[","")
   #eliminamos los ] de la variable 
  key=key.replace("]","")
   #eliminamos los ( de la variable 
  key=key.replace("(","")
   #eliminamos los ) de la variable 
  key=key.replace(")","")
   #eliminamos los " de la variable 
  key=key.replace('"',"")
   #eliminamos los ' de la variable 
  key=key.replace("'","")
   #imprimimos los valores de la variable 
  print key 
  
  #los valores se imprimiran en consola en caso de desear un archivo de texto usar el modificador >>nomnbreArchivo.txt 
  #escrito a continuacion de la orden de compilacion ejemplo (~#pyhton archi.py>>archivo.txt)
