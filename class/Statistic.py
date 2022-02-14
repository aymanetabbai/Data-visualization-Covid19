# -*- coding: utf-8 -*-
"""
Created on Sat May  8 19:31:56 2021

@author: hassi
"""
import numpy as np
import LoadData as l
import Transformations as t
class statistic():
     def __init__(self, MatrixData,item):
         """
         

         Parameters
         ----------
         MatrixData : Liste
             Il s'agit d'une liste de listes.

         Returns
         -------
         None.

         """
         self.MatrixData=MatrixData
         self.item=item
                 
     def mean(self):
          '''
          Cette méthode prend en paramètre une liste de données et renvoie
          la moyenne de la variable item .

          Parameters
          ----------
          item : str
              Le nom de la variable dont on veut calculer la moyenne.

          Returns
          -------
          reel
              La moyenne de la variable item .

          '''
          
          m=0
          a=t.Data(self.MatrixData).get_values_in_item(self.item)
          n=len(a)
          for i in range(n):
            m=m+int(a[i])
          return m/n
     def variance(self):
        '''
         
          Cette méthode prend en paramètre une liste de données et renvoie
          la variance de la variable item 
         Parameters
         ----------
         item : str
             Il s'agit du nom de la variable dont on veut calculer
             la variance.

         Returns
         -------
         m : reel
             la variance de la variable item.

         '''
       
        m=0
        a=t.Data(self.MatrixData).get_values_in_item(self.item)
        n=len(a)
        for i in range(n):
            m=m+int(a[i])**(2)
        m=m/n-self.mean()**(2)
        return m
     def ecart_type(self):
         '''
         
         
          Cette méthode prend en paramètre une liste de données et renvoie
          l'écart type de la variable item 
         
         Parameters
         ----------
         item : TYPE
             Il s'agit du nom de la variable dont on veut calculer
             l'écart-type.

         Returns
         -------
         reel
             l'écart-type de la variable item.

         '''
         return np.sqrt(self.variance())
     
     

    

    
class moyenne_gliss():
    def __init__(self, MatrixData, ordre,item):
        '''
        

        Parameters
        ----------
        MatrixData : 
            DESCRIPTION.
        ordre : entier
            Il s'agit de la plage sur laquelle on veut calculer la moyenne.
        item : str
            Il s'agit du nom de la variable dont on veut calculer
             la moyenne glissante .

        Returns
        -------
        None.

        '''
        self.MatrixData=MatrixData
        self.ordre=ordre
        self.item=item
    def moyenne_glissante(self):
        '''
        

        Returns
        -------
        liste_moyennes : liste
            Il s'agit d'une liste des différentes moyenne en prenat en 
            considération l'ordre.

        '''
        valeurs=t.Data(self.MatrixData).get_values_in_item(self.item)
        valeurs_int=[]
        for i in valeurs:
          valeurs_int.append(float(i))
        indice_debut = (self.ordre - 1) // 2
        liste_moyennes = [sum(valeurs_int[i - indice_debut:i + indice_debut + 1]) / self.ordre for i in range(indice_debut, len(valeurs) - indice_debut)]
        return liste_moyennes
