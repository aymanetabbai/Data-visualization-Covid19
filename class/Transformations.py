# -*- coding: utf-8 -*-
"""
Created on Tue May 11 14:28:18 2021

@author: hassi
"""

class Data:
    '''Cette classe représente et permet de manipuler notre liste de données ''' 

    def __init__(self, MatrixData):
        self.MatrixData = MatrixData
   
    def get_items(self):
        '''
        

        Returns
        -------
        Liste
            Cette méthode retourne le nom des variables de nos données.

        '''
        return self.MatrixData[0]
    
    def get_values_in_item(self, item):
        '''
        

        Parameters
        ----------
        item : str
            Il s'agit du nom de la variable dont on veut récuperer les
            observations.

        Returns
        -------
        observations : liste
            Elle selectionne l'ensemble des valeurs de la variable 'item'
            de notre liste de données.

        '''
        k =self.MatrixData[0].index(item)
        observations=[]
        for enregistrement in self.MatrixData[1:]:
            observations.append(enregistrement[k])
        return observations
    
    '@abstractmethod'
    def get(self):
        pass
    pass


class Df_window(Data):
    def __init__(self, MatrixData,start,end):
        '''
        

        Parameters
        ----------
        MatrixData : TYPE
            DESCRIPTION.
        start : Date
            Il s'agit de la date à partir de la quelle on souhaite sélectionner
            nos données..
        end : Date
            Il s'agit de la date de fin des données qu'on veut sélectionner..

        Returns
        -------
        None.

        '''
        super().__init__(MatrixData)
        self.start=start
        self.end=end
    def get(self):
        '''
        Cette méthode permet de  sélectionner les donnés où la date est
        entre start et end


        Returns
        -------
        resultat : Liste
            Il s'agit d'une liste de listes telles que les listes représentent
            les observations entre les dates start et end,les dates start et end sont
            incluses.

        '''
        resultat=[]
        resultat.append(self.MatrixData[0])
        indice=self.MatrixData[0].index('jour')
        for enregistrement in self.MatrixData:
            if enregistrement[indice]<= self.end and enregistrement[indice] >= self.start  :
                resultat.append(enregistrement)
        return resultat
        
class Df_where(Data):
    def __init__(self, MatrixData,item,value):
        '''
        

        Parameters
        ----------
        MatrixData : TYPE
            DESCRIPTION.
        item :str
        value : str

        Returns
        -------
        None.

        '''
        super().__init__(MatrixData)
        self.item=item
        self.value=value
    def get(self):
        '''
        Cette méthode permet de  sélctionner les donnés où item est
        égale à value
        
        Returns
        -------
        resultat : liste
            liste des données dont la varible item égale value.

        '''
        resultat=[]
        resultat.append(self.MatrixData[0])
        indice = self.MatrixData[0].index(self.item)
        for enregistrement in self.MatrixData:
            if enregistrement[indice]==self.value:
               resultat.append(enregistrement)
        return resultat 

class Df_sumby(Data):
    ''' cette classe permet de manipuler nos données '''
    def __init__(self, MatrixData,item):
        super().__init__(MatrixData)
        self.item=item
    def sumby(self):
        """
            Cette méthode perment de retourner la somme des valeurs de
            la variable item

        Returns
        -------
        somme:float.
            Il s'agit de la sommes des observations de la variable item'

        """
        somme=0
        observations=self.get_values_in_item(self.item)
        for i in observations:
            somme=somme+int(i)
        print(somme)
        return(somme)