import re
file=open("pichincha.json")
texto=file.read()
file.close()
#print texto
patron = re.compile(ur'created_at":([^,]+),"f[^j]*[^\[]+([^}]+)')
text='u'+texto
m=re.findall(patron,texto)
negras=("{","}","[","]")
print len(m)

