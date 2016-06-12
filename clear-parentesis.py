import re
file=open("quito.couch")
texto=file.read()
file.close()
#print texto
patron = re.compile(ur'created_at":([^,]+),"f[^j]*[^\[]+([^}]+)')
text='u'+texto
m=re.findall(patron,texto)
negras=("{","}","[","]")
print len(m)
for x in m:
  key=str(x)	
  key=key.replace("[","")
  key=key.replace("]","")
  key=key.replace("(","")
  key=key.replace(")","")
  key=key.replace('"',"")
  key=key.replace("'","")
  print key 
