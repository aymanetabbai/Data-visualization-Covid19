# -*- coding: utf-8 -*-
"""
Created on Sun May  9 13:36:13 2021

@author: hassi
"""
import Vacances as v 
import LoadData as l
import Transformations as t
import Statistic as s
from kmeans import KMeans
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time
import Export as e






#Combien de nouvelles hospitalisations ont eu lieu ces 7 derniers jours dans chaque département?
b=t.Df_window(l.covid_dep,"2021-02-24","2021-03-03")
test=b.get()
nbr_hospitalisation_departemental={}
for k in range(1,102):
    
    test_dep=t.Df_where(test,"dep", test[k][0]).get()
    a=t.Df_sumby(test_dep,"incid_hosp").sumby()
    nbr_hospitalisation_departemental[test[k][0]]=a
    d=e.Export("nouvelle hospitalisations dans le departement "+ test[k][0],a)
    d.exporter("stockage5.csv")
    
#Comment évolue la moyenne des nouvelles hospitalisations journalières de cette semaine par rapport à
#celle de la semaine dernière ?

#Question 4 K means

'''on commence par extraire le jeux donnees sure la date 2020-12-29","2021-02-03 
pour pouvoir calculer la moyenne glissante sur les le premier jour et le dernier jour
'''

b=t.Df_window(l.covid_dep,"2020-12-29","2021-02-03")
b1=b.get()
  

donnes=[]        
for i in range(1,102) : #boucle sur les departement pour extraire les donnees sur chaque dep 
    test_dep=t.Df_where(b1,"dep", test[i][0])
    test_dep1=test_dep.get()
    K=[]
    for j in range(2,6) :          #boucle sur les variables
        moyglis=s.moyenne_gliss(test_dep1,7,test[0][j]).moyenne_glissante()
        #moyenne glissante de lma i-eme dep sur la j-eme variable
        K=K+moyglis #stocker les les moyennes glissantes pourtout les variables de chaque dep
    donnes.append(K) #stocker les moyennes glissantes des depart


     
covid2=np.array(donnes) #transformation en array
k=KMeans(K=3,max_iteration=100,graph=False)# creer l'objet de la classe kmeans

t_pred=k.predict(covid2)#predire le regroupement avec la fonction predict
departement=t.Data(b1).get_values_in_item("dep")[:101]#list des dep
#presentation des resultats sous forme de dictionnaire
d={}
d["groupe1"]=[]
d["groupe2"]=[]
d["groupe3"]=[]
for i in range (0,len(departement)) :
    if t_pred[i]==0 :
        d["groupe1"].append(departement[i])
    elif t_pred[i]==1 :
        d["groupe2"].append(departement[i])
    else :
        d["groupe3"].append(departement[i])                            
for keys in d :
    for i in d[keys] :
        z=e.Export("le departement "+str(i),str(keys))
        z.exporter("stockage5.csv")
    

                                

#question 5
#fonction qui calcule la somme selon la variable choisie durant une periode lié au vacance:

vac=v.Vacances(l.vacances)
(x,y)=vac.date_vacance_decale("Vacances de la Toussaint","2020-2021","Zone A",7)
periode_tous=b=t.Df_window(l.covid_dep,x,y)
rea=periode_tous.get()
reanimationvac=t.Df_sumby(rea,"incid_rea").sumby()
r=e.Export("nombre totale  de réanimation peadant la semaine suivant les Vacances de la Toussaint ",reanimationvac)
r.exporter("stockage5.csv")

covid_sans_sexe=t.Df_where(l.covid_sexe,'sexe','0').get()
covid_sans_sexe_dep01=t.Df_where(covid_sans_sexe,'dep','01').get()
liste_date_données=t.Data(covid_sans_sexe_dep01).get_values_in_item('jour')
liste_moyennes=[]
liste_dates_de_moyennes=[]
for i in range(0,345,6):
 donnes_7=t.Df_window(l.covid_dep,liste_date_données[i],liste_date_données[i+6]).get()
 liste_dates_de_moyennes.append(liste_date_données[i]+' '+liste_date_données[i+6])
 e=t.Df_sumby(donnes_7,'incid_hosp')
 z=e.sumby()
 liste_moyennes.append(z/7)
plt.bar(range(58) ,liste_moyennes, width = 0.5, color = 'red')