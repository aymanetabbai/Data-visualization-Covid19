#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 13:30:31 2021

@author: aymanetabbai
"""
import LoadData as l
import datetime


class Vacances :    
    def __init__(self, dic_data):
        '''
        cette classe nous permet de manipuler le fichier json

        Parameters
        ----------
        dic_data : dictionnaire
            dictionnaire qui contient la calendrier des vacances scolaires.

        Returns
        -------
        None.

        '''
        self.dic_data = dic_data
        
    
    def date_vacance_decale(self,nom,annees,zone,dec=0) :
        '''
        cette methode nous permet de retourner une periode decale apres ou avant date des vacances '

        Parameters
        ----------
        nom : str
            nom des vacances.
        annees : str
            annee scolaire.
        zone : str
            zone du departement.
        dec : float
            nombre de jours de decalage. par defut 0.

        Returns
        -------
        str
            date de debut de la perode.
        TYPE
            date de fin de la periode.

        '''
        calendrier=l.vacances["Calendrier"]
        for i in range (0,len(calendrier)) :
            
        
            if calendrier[i]['Description']==nom and calendrier[i]['annee_scolaire']==annees and calendrier[i]['Zone']==zone :
                
                (x,y)=(calendrier[i]['Debut'],calendrier[i]['Fin'])
                if dec==0 :
                    return (x,y)
                if dec>0 :                   
                    z=datetime.datetime.strptime(y, '%Y-%m-%d')
                    fin =z+datetime.timedelta(days=dec)
                    fin1=str(fin.strftime("%Y")+"-"+fin.strftime("%m")+ "-"+fin.strftime("%d"))
                    return (y,fin1)
                else :
                    z=datetime.datetime.strptime(x, '%Y-%m-%d')
                    debut=z+datetime.timedelta(days=dec)
                    debut1=str(debut.strftime("%Y")+"-"+debut.strftime("%m")+ "-"+debut.strftime("%d"))
                    return (debut1,x)
