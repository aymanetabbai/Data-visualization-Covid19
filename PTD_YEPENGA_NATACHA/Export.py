#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 13:56:55 2021

@author: aymanetabbai
"""
import csv

class Export:
    def __init__(self, name, value):
        '''
        cette classe permet de generer un fichier csv avec deux collone 

        Parameters
        ----------
        name : str
            le nom du resultat.
        value : float
            la valeur numerique .

        Returns
        -------
        None.

        '''
        self.name = name
        self.value = value
    
    def exporter(self,filename):
        '''
        cette methode permet d'exporter stocker les parametres de l'objet Export dans un fichier csv' '

        Parameters
        ----------
        filename : str
            chemin du fichier .csv.

        Returns
        -------
        None.

        '''

        with open(filename,'a',newline='') as f:  
            #Ajout d'une ligne dans le fichier csv
            ecrire=csv.writer(f,delimiter=';')                             # préparation à l'écriture   
               # Mettre dans écrire cette nouvelle ligne
            ecrire.writerow([str(self.name),str(self.value)]) 
        
        

