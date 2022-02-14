# -*- coding: utf-8 -*-
"""
Created on Sat May  8 19:17:43 2021

@author: hassi
"""

import csv
import json
class ReadFile:
    ''' Cette classe représente les fichiers excel et json importé 
    Un objet de cette classe est initialisé par le nom du fichier
    qu'on souhaite importer'''

    def __init__(self, filename):
        '''
        

        Parameters
        ----------
        filename :  str
            Il s'git du nom du fichier qu'on veur impoter

        Returns
        -------
        None.

        '''
        self.filename = filename

    def open_csv(self) :
        '''
        

        Returns
        -------
        data : list
            cette méthode  retournenotre ensemble de données sous
            forme d'une liste de listes d'observations  .

        '''
        data=[]
        with open(self.filename, encoding='ISO-8859-1') as csvfile:
            covidreader = csv.reader(csvfile, delimiter=";")
            for row in covidreader:
                data.append(row)
        return (data)

    def open_json(self):
        with open(self.filename) as jsonfile:
            datajson = json.load(jsonfile)
        return datajson



incid_reg=ReadFile("covid-hospit-incid-reg-2021-03-03-17h20.csv").open_csv()
service_hospitalier_covid=ReadFile("donnees-hospitalieres-etablissements-covid19-2021-03-03-17h03.csv").open_csv()
covid_classeage=ReadFile("donnees-hospitalieres-classe-age-covid19-2021-03-03-17h03.csv").open_csv()
covid_sexe=ReadFile("donnees-hospitalieres-covid19-2021-03-03-17h03.csv").open_csv()
covid_dep=ReadFile("donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv").open_csv()
vacances=ReadFile("VacancesScolaires.json").open_json()




    

    

        

