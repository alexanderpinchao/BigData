import re
file=open("compendio.txt")
texto=file.read()
file.close()
patron=re.compile(ur'(\D*\s+\D+\s+\d+\s+\d+:\d+:\d+\s\D\d+\s\d+),\s(\D\d+\D\d+),(\D\d+\D\d+),(\D*\d+\D\d+),(\D*\d+\D\d+),(\D*\d+\D\d+),(\D*\d+\D\d+),(\D*\d+\D\d+),(\D*\d+\D\d+)\s')
text='u'+texto
m=re.findall(patron,text)
pat=re.compile(ur"[A-Za-z]*")
for x in m:
   lat1=float(str(x[3]))
   lat2=float(str(x[5]))
   if(lat1>lat2):
    lattot=lat2+(lat1-lat2)/2
   else:
    lattot=lat1-(lat1-lat2)/2
   lon1=float(str(x[2]))
   lon2=float(str(x[4]))
   if(lon1>lon2):
    lontot=lon2+(lon1-lon2)/2
   else:
    lontot=lon1-(lon1-lon2)/2
   print str(x[0])+","+str(lattot)+","+str(lontot)
   
 
