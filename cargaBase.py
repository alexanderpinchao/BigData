import time
import re
import couchdb
import json

file =open("latlon.txt")
texto=file.read()
file.close()
server = couchdb.Server('http://localhost:5984/')
try:
    db = server.create('coordenadas')
except:
    db = server['coordenadas']
patron=re.compile(ur'\s(\D{3})\s\D+\s\d+\s(\d+):\d+:[^,]+,([^,]+),(\D\d\D\d+)')
m=re.findall(patron,texto)
for x in m:
  ingreso='{"dia":"'+str(x[0])+'","hora":"'+str(int(x[1]))+'","coordenadas": {"latitud": '+str(x[3])+',"logitud": '+str(x[2])+'}}'
  ingres_json=json.loads(ingreso)
  doc=db.save(ingres_json)
  
