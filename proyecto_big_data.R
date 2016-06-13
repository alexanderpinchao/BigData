#codigo creado por: Polanco Boris
#fecha: 10 de junio del 2016
#Cargamos las librerías necesarias para el anàlisis y construcciòn de mmapas
library(leaflet)#Esta libreria es para usar mapas de openstreetmap
library(readxl)#Esta librerìa es para leer archivos de excel
library(data.table)#Esta librerìa nos ayuda a trabajar con gran cantidad de informacion de manera mas rapida
setwd("C:/Users/Usuario/Desktop")
#Leemos el archivo hotspots.csv, este archivo contiene información de los hotspots municipales en la ciudad de quito
wifi_quito<- data.frame(fread("hotspots.csv",colClasses = c("numeric","numeric","numeric","character","character","character")))

#Generamos un mapa m, donde se señala los hotsposts en la ciudad de Quito
m <- leaflet() %>%
  addTiles() %>%  # Add default OpenStreetMap map tiles
   addMarkers(lng=wifi_quito$Longitud[1:268], lat=wifi_quito$Latitud[1:268], popup=wifi_quito$Sector[1:268])
m
#Leemos el archivo donde se encuentra 40000 tweets georefenreciados 
tweets<-read_excel("tweets.xlsx")

#####Generamos un mapa con la información de tales tweets

m <- leaflet() %>%
  addTiles() %>%  # Add default OpenStreetMap map tiles
  addMarkers(lng=wifi_quito$Longitud[1:268], lat=wifi_quito$Latitud[1:268], popup=wifi_quito$Sector[1:268],icon = ship)%>%
    addCircleMarkers(lng=tweets$Longitud[1:40000], lat=tweets$Latitud[1:40000],
       stroke = FALSE, fillOpacity = 0.2,color = c("blue","red"),radius=4
  )

m

####Función para calcular la distancia entre dos coordenadas.
#cargamos el paquete geosphere que incluye una función para calcular la distancia entre dos coordenadas

library(geosphere)
names(wifi_quito)
#Genero una lista de distancias entre cada tweet y cada hotspot (esto demora aproximadamente 15 min)
matriz_distancias<-vector(mode="list", 40000)
for(i in 1:40000)
  for(k in 1:268){
matriz_distancias[[i]][k]<-distGeo(c(tweets[i,1],tweets[i,2]),c(wifi_quito$Longitud[k],wifi_quito$Latitud[k]))/1000
  }
#a la lista la hacemos matriz
matriz_distancias2<-data.frame(matriz_distancias)
colnames(matriz_distancias2)<-paste("tweet_",1:40000)
#Extraigo las distancias minimas de entre el tweet y el hotspot
apply(matriz_distancias2,2,FUN = function(x)min(x[x>0]))
htweet<-apply(matriz_distancias2,2,FUN = function(x)which.min(x))
write.csv(data.frame(unlist(htweet)),"htweet.csv")
data.frame(table(data.frame(unlist(htweet))))[,2]

#Se genera una tabla de frecuencia para saber cuantos tweets recepto cada hotspot
nrotw<-data.frame(table(data.frame(unlist(htweet))))
names(nrotw)<-c("Wifi.ID","Freq")
wifi_quito<-merge(wifi_quito,nrotw,by="Wifi.ID")
names(wifi_quito)

#Mapa_FINAL: En este mapa generamos los hotspots donde se señala con circulos rojos los
#hotspots con una menor recepción de tweets, (entre cero y 100) verde menor a 300, y azul mas de 300

m <- leaflet() %>%
  addTiles() %>%  # Add default OpenStreetMap map tiles
    addCircleMarkers(lng=wifi_quito$Longitud[1:268], lat=wifi_quito$Latitud[1:268],
                   stroke = FALSE,fillOpacity = 0.5,
                   color = ifelse(wifi_quito$Freq<=100, "red", ifelse(wifi_quito$Freq<=300,"green","blue")),
                   radius = ifelse(wifi_quito$Freq<=100,4, ifelse(wifi_quito$Freq<=300,8, 15)),
                   popup=paste(sep = "<br/>",as.character(wifi_quito$Sector[1:268]),paste("# Tweets: ",as.character(wifi_quito$Freq[1:268]))))
m

