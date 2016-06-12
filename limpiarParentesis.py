import re
file=open("quitoSmile.json")
texto=file.read()
file.close()
patron = re.compile(ur'created_at":([^,]+),"f[^j]*[^\[]+([^}]+)')
text='u'+texto
m=re.findall(patron,texto)
negras=("{","}","[","]")
for x in m:
  key=str(x)	
  key=key.replace("[","")
  key=key.replace("]","")
  key=key.replace("(","")
  key=key.replace(")","")
  key=key.replace('"',"")
  key=key.replace("'","")
  print key 
