import os
from os import error
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
#/Users/david/Desktop/titanic/dataset.xls
#python -m pip install <package>

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def chooseFormat():
    choix=input("choix du format : (excel|json|csv) ")
    if (choix=="excel"):
        fichier=input('Entrez le chemin d\'accès au fichier  : ')
        if ( os.path.exists(fichier) and os.path.isfile(fichier) and fichier[-4:]=='.xls'):
            return pd.read_excel(fichier)
        else:
            print("Erreur fichier")
            return chooseFormat()
    elif (choix=="json"):
        fichier=input('Entrez le chemin d\'accès au fichier  : ')
        if ( os.path.exists(fichier) and os.path.isfile(fichier) and fichier[-5:]=='.json'):
            return pd.read_json(fichier)
        else:
            print("Erreur fichier")
            return chooseFormat()
    elif (choix=="csv"):
        fichier=input('Entrez le chemin d\'accès au fichier  : ')
        if ( os.path.exists(fichier) and os.path.isfile(fichier) and fichier[-4:]=='.csv'):
            return pd.read_csv(fichier)
        else:
            print("Erreur fichier")
            return chooseFormat()
    else:
        return pd.DataFrame()

def dropColumn(dataset):
    firstChoice=input("Voulez-vous supprimer des colonnes ? (oui|non) ")
    if (firstChoice=="oui"):
        listRemove=[]
        listColumn=dataset.columns.tolist()
        for i in listColumn:
            while True:
                column=input("voulez vous supprimez la colonne "+i+" : (oui|non) ")
                if (column=='oui'):
                    listRemove.append(i)
                if(column!='oui' and column!='non'):
                    print("mauvaise entrée")
                if(column=='oui' or column=='non'):
                    break  
        return dataset.drop(listRemove,axis=1)
    elif (firstChoice!='oui' and firstChoice!='non'):
        print("mauvaise entrée")
        return dropColumn(dataset) 
    else:
        return dataset


def verifyEmptyLine(dataset):
    listColumnNotFull=[]
    listColumn=dataset.columns.tolist()
    listVerify= dataset.isnull().any() 
    incr=0
    for i in listVerify:
         if (i==True):
             listColumnNotFull.append(listColumn[incr])
         incr+=1
    if ( len(listColumnNotFull)>0):
        fisrtChoice=input("Il manque des valeurs dans votre dataframe, Voulez-vous supprimer les lignes avec des valeurs nulles ? (oui|non) ")
        if(fisrtChoice=="oui"):
            return deleteEmptyValues(dataset)
        elif(fisrtChoice=="non"):
            return dataset
        else:
            return verifyEmptyLine(dataset)
    else:
        return dataset
 

    
              
     
def fullValues(dataset,column):
    return dataset.fillna(dataset[column].mean())

def deleteEmptyValues(dataset):
    return dataset.dropna(axis=0)

def describeValues(dataset):
    return dataset.describe()

def sampleValue(dataset):
    return dataset.sample()

def correlationColumn(dataset):
    return dataset.corr()

def dataframeInfos(dataset):
    print("Nombre de lignes et colonnnes dans le dataframe : ",dataset.shape)
    print("Nombre d'éléments dans le dataframe : ",dataset.size)
    print("Dimension du dataframe : ",dataset.ndim)
    return dataset.info()



def countValues(dataset):
    listColumn=dataset.columns.tolist()
    column = input ("entrez la colonne qui vous intéresse : ")
    if(column not in listColumn):
        print("Nom de colonne incorrecte ")
        return countValues(dataset)
    return dataset[column].value_counts()

def meanValue(dataset):
    listColumn=dataset.columns.tolist()
    column = input ("entrez la colonne qui vous intéresse : ")
    if(column not in listColumn):
        print("Nom de colonne incorrecte ")
        return meanValue(dataset)
    return dataset[column].mean()

def countValuesGraph(dataset):
    listColumn=dataset.columns.tolist()
    column = input ("entrez la colonne qui vous intéresse : ")
    if(column not in listColumn):
        print("Nom de colonne incorrecte ")
        return countValuesGraph(dataset)
    return dataset[column].value_counts().plot.bar()

def valuesHist(dataset):
    listColumn=dataset.columns.tolist()
    column = input ("entrez la colonne qui vous intéresse : ")
    if(column not in listColumn):
        print("Nom de colonne incorrecte ")
        return valuesHist(dataset)
    return dataset[column].hist()

def groupbyMean(dataset):
    listGroup=[]
    list=dataset.columns.tolist()
    for i in list:
        while True:
            column=input("voulez vous utiliser la colonne "+i+" : (oui|non) ")
            if (column=='oui'):
               listGroup.append(i)
            if (column!='oui' and column!='non'):
                 print("mauvaise entréee")
            if (column=="oui" or column=="non"):
                break
    return dataset.groupby(listGroup).mean()
           


def presentation(dataset):
    print("Les actions possibles : ")
    print("1. Afficher les données statistiques du Dataframe")
    print("2. Obtenir la corrélation entre colonne : ")
    print("3. Afficher les réptitions d\'une colonne")
    print("4. Afficher la moyenne d\'une colonne")
    print("5. Obtenir un graphique")
    print("6. Obtenir un histographe")
    print("7. Analyse statisque par regroupement de colonne ")
    print("8. Obtenir un échantillon du dataframe ")
    print("9. Afficher les informations du dataframe")
    choix = input('Entrez votre choix: (1|2|3|4|5|6|7|8|9) ')
    if (choix=='1'):
        print(describeValues(dataset))
    elif(choix=='2'):
        print(correlationColumn(dataset))
    elif (choix=='3'):
        print(countValues(dataset))
    elif (choix=='4'):
        print(meanValue(dataset))
    elif (choix=='5'):
        print(countValuesGraph(dataset))
        print(plt.show())
    elif (choix=='6'):
        print(valuesHist(dataset))
        print(plt.show())
    elif (choix=='7'):
        print(groupbyMean(dataset))   
    elif (choix=='8'):
        print(sampleValue(dataset)) 
    elif (choix=='9'):
        print(dataframeInfos(dataset))
    else:
        print ("mauvaise entrée")
        presentation(dataset)

    

def lancerLeProgramme():
    print ("Bienvenue")
    dataset= chooseFormat()
    if dataset.empty:
        print("format non supporté")
        lancerLeProgramme() 
    else:
        dataset=dropColumn(dataset)
        dataset=verifyEmptyLine(dataset)
        print(dataset.head())
        while True:
           action= input("Voulez-vous réaliser une action ? (oui|non) ")
           if (action=="oui"):
             presentation(dataset)
           elif(action=="non"):
               print("Bye Bye")
               break
           else:
               print("mauvaise entrée")
               


    

lancerLeProgramme()   
