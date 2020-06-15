# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:21:10 2020

@author: osman
"""

import pandas as pd
import numpy as np

data = pd.read_csv('adult.csv')


def orderWorkclass(col):
    """
    params : col (Pandas.Series) -> colonne du dataframe contenant les infos sur 
                    workClass
                    
    
    return : Retourne la colonne transformer (Pandas.Series)

                
    description : transforme la colonne WorkClass qui de Type String
                et le transforme en numerique selon le dictionnaire
                
                Le dictionnaire a été crée en regradant l'analyse
                graphique ainsi que les pourcentage des revenu inf
                à 50K de chaque catégorie.
            
    """
    
    dico = {
        'Self-emp-inc' : 0,
        'Federal-gov' : 1,
        'Local-gov' : 2,
        'Self-emp-not-inc' : 3,
        'State-gov' : 4,
        'Private' : 5,
        'Without-pay' : 6
        }
    
    return col.apply(lambda x: dico[x])


def orderRelation(col):
    
    """
        params : col (Pandas.Series) -> colonne du dataframe contenant les infos sur 
                    relationship
                    
    
    return : Retourne la colonne transformé (Pandas.Series)

                
    description : transforme la colonne Relationship qui est de Type String
                et le transforme en numerique selon le dictionnaire
                
                Le dictionnaire a été crée en regradant l'analyse
                graphique  des revenu inf à 50K de chaque catégorie.
            
    """
    
    dico = {
        'Wife' : 0,
        'Husband' : 1,
        'Not-in-family' : 2,
        'Unmarried' : 3,
        'Own-child' : 4,
        'Other-relative' : 5
    }
    
    return col.apply(lambda x: dico[x] )
        
    
def orderRace(col):
    """
       params : col (Pandas.Series) -> colonne du dataframe contenant les infos sur 
                        la race
                        
        
        return : Retourne la colonne transformé (Pandas.Series)
    
                    
        description : transforme la colonne Race qui est de Type String
                    et le transforme en numerique selon le dictionnaire
                    
                    Le dictionnaire a été crée en regradant l'analyse
                    graphique  des revenu inf à 50K de chaque catégorie.
                
    """
    dico = {
        'White': 0,
        'Asian-Pac-Islander': 1,
        'Amer-Indian-Eskimo' : 2,
        'Black' : 3,
        'Other' : 4
        }
    
    return col.apply(lambda x: dico[x])


def orderMaritalStatus(col):
    
    """
       params : col (Pandas.Series) -> colonne du dataframe contenant les infos sur 
                        l'état civil
                        
        
        return : Retourne la colonne transformé (Pandas.Series)
    
                    
        description : transforme la colonne marital status qui est de Type String
                    et le transforme en numerique selon le dictionnaire
                    
                    Le dictionnaire a été crée en regradant l'analyse
                    graphique  des revenu inf à 50K de chaque catégorie.
            
    """
    
    dicot = {
        'Married-civ-spouse' : 0,
        'Married-AF-spouse' : 1,
        'Never-married' : 2,
        'Divorced' : 3,
        'Widowed' : 4,
        'Separated' :5,
        'Married-spouse-absent': 6
    }
    return col.apply(lambda x: dicot[x])








def orderOccup(col):
    
    """
           params : col (Pandas.Series) -> colonne du dataframe contenant les infos sur 
                                       le poste
                        
        
            return : Retourne la colonne transformé (Pandas.Series)
    
                    
            description : transforme la colonne Occupation qui est de Type String
                    et le transforme en numerique selon le dictionnaire
                    
                    Le dictionnaire a été crée en regradant l'analyse
                    graphique  des revenu inf à 50K de chaque catégorie.
                
    """
    
    dico ={
        'Exec-managerial': 0,
        'Prof-specialty':1,
        'Sales':2,
        'Craft-repair':3,
        'Adm-clerical':4,
        'Tech-support':5,
        'Transport-moving':6,
        'Protective-serv':7,
        'Machine-op-inspct':8,
        'Farming-fishing':9,
        'Handlers-cleaners':10,
        'Other-service':11,
        'Armed-Forces':12,
        'Priv-house-serv':13
        }
    
    
    return col.apply(lambda x: dico[x])

def transform(df):
    
    df['workclass'] = orderWorkclass(df.workclass)
    print('Workclass column transformed')
    
    df['sex'] = df.sex.apply(lambda x: 0 if x == 'Male' else 1)
    print('Sex Column transformed')
    
    df['relationship'] = orderRelation(df.relationship)
    print('Relationship column transformed')
    
    df['race'] =orderRace(df.race)
    print('Race column transformed')
    
    df['marital.status'] = orderMaritalStatus(df['marital.status'])
    print('Martial Status column transformed')
    
    df['occupation'] = orderOccup(df.occupation)
    print('Occupation column transformed')
