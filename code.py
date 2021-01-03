#!/usr/bin/python3.6
 
import http.client
import bs4 as bs
import urllib.request
from matplotlib import pyplot as plt
 
 
site="www.top500.org"
 
 
site_liste="https://" +site+"/lists/top500"
 
source=urllib.request.urlopen(site_liste).read()
soup=bs.BeautifulSoup(source,'lxml')
 
#accesez pagina cu toate topurile
containers=soup.find_all('ul',{"id":"squarelist"})
years_page=containers[0]
 
 
verificare_exceptie=1
k=0
medie_an=0
contor_luna=0
contor_an=0
an1=2020
an2=2019
contor_scadere_an=0
 
axa_an=[]
axa_performanta=[]
contor1=0
contor_td=1
eroare_prima_luna=0

#caut linkul fiecarei pagini care are un top
for url in years_page.find_all('a'):
 verificare_exceptie=1
 #creez linkul fiecarei pagini care are top
 link=site_liste+"/"+url.get('href')
 k=k+1
 contor1=contor1+1
 if contor1==2:
   sir_an=url.get('href')[0:4]
   axa_an.append(int(sir_an))
   contor1=0
 try:
   urllib.request.urlopen(link).read()
 except:
   verificare_exceptie=0
 
 if verificare_exceptie==0:
   if contor_luna==0:
     eroare_prima_luna=1
   elif contor_luna==1:
     medie_an=medie_luna
     contor_luna=0
     axa_performanta.append(medie_an)
     medie_an=0.0
 
 if verificare_exceptie==1:
   source1=urllib.request.urlopen(link).read()
   soup1=bs.BeautifulSoup(source1,'lxml')
  
 
   tds=soup1.find_all('td')
 
   #retin doar td-urile primelor 3 clasate
   tds=tds[:18]
 
   contor_rank=0
   nr=0
   ok=0
   medie_luna=0.0
   for td in tds:
 
     #selectez si modifc in int rmax-ul primelor 3 clasate
     if contor_rank==3 and ok==0:
       aux=str(td)
       aux=aux[31:(len(aux)-5)]
       if aux.find(',')==-1:
         pass
       else:
         aux=aux.split(',')
         nr=int(aux[0])*1000
         aux=aux[1]
       aux=aux.split('.')
       nr=nr+int(aux[0])
       aux=aux[1]
       nr=nr+(int(aux)/10)
       medie_luna=medie_luna+nr
       contor_rank=0
       ok=1
     elif ok==0:
       contor_rank=contor_rank+1
     if contor_rank==6 and ok==1:
       aux=str(td)
       aux=aux[31:(len(aux)-5)]
       if aux.find(',')==-1:
         pass
       else:
         aux=aux.split(',')
         nr=int(aux[0])*1000
         aux=aux[1]
       aux=aux.split('.')
       nr=nr+int(aux[0])
       aux=aux[1]
       nr=nr+(int(aux)/10)
       medie_luna=medie_luna+nr
       #print(medie_luna)
       contor_rank=0
       ok=1
       contor_rank=1
     elif ok==1:
       contor_rank=contor_rank+1
 
   #calculez media pe luna,respectiv pe an
   contor_luna=contor_luna+1
   medie_luna=medie_luna/3
 
   if eroare_prima_luna==1:
     medie_an=medie_luna
     axa_performanta.append(medie_an)
     medie_an=0.0
     contor_luna=0
     eroare_prima_luna=0
   elif eroare_prima_luna==0:
     medie_an=medie_an+medie_luna
    
     if contor_luna==2:
       medie_an=medie_an/2
       axa_performanta.append(medie_an)
       contor_luna=0
       medie_an=0.0
an1=2020
an2=2019
progres_mediu=0
for i in range(len(axa_performanta)-1):
 an1=an1-1
 an2=an2-1
 progres_mediu=progres_mediu+(axa_performanta[i]/axa_performanta[i+1])
progres_mediu=progres_mediu/len(axa_performanta)
print("Progresul mediu este: ",progres_mediu,end='\n')     
 
#Plotting to our canvas
fig=plt.figure(figsize=(20,10))
 
plt.plot(axa_an,axa_performanta)
plt.title('Grafic evolutia performantei calculatoarelor',fontsize=15)
plt.ylabel('Performanta(RMAX)',fontsize=15)
plt.xlabel('An',fontsize=15)
 #Showing what we plotted
plt.show()

