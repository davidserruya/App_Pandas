import os
from os import error
import pandas as pd
from matplotlib import pyplot as plt
#from term2web import *
#/Users/david/Desktop/titanic/dataset.xls
#python -m pip install <package>

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
    firstChoice=input("Voulez-vous supprimer des colonnes ? (oui|non)")
    if (firstChoice=="oui"):
        listRemove=[]
        print(listRemove)
        listColumn=dataset.columns.tolist()
        print(listColumn)
        for i in listColumn:
            column=input("voulez vous supprimez la colonne "+i+" : (oui|non) ")
            if (column=='oui'):
               listRemove.append(i)
            elif (column!='oui' and column!='non'):
                print("mauvaise entrée")
                return dropColumn(dataset)
        return dataset.drop(listRemove,axis=1)
    elif (firstChoice!='oui' and firstChoice!='non'):
        print("mauvaise entrée")
        return dropColumn(dataset) 
    else:
        return dataset


def verify(dataset):
    listColumnNotFull=[]
    listColumn=dataset.columns.tolist()
    listVerify= dataset.isnull().any() 
    incr=0
    for i in listVerify:
         if (i==True):
             listColumnNotFull.append(listColumn[incr])
         incr+=1
    if ( len(listColumnNotFull)>0):
        fisrtChoice=input("Il manque des valeurs dans votre dataframe, Voulez-vous le modifier? (oui|non)")
        if(fisrtChoice=="oui"):
            secondChoice=input("Par suppression ou harmonisation ? (sup|har)")
            if (secondChoice=="sup"):
                return dropValues(dataset)
            elif(secondChoice=="har"):
                for b in listColumnNotFull:
                    if (dataset[b].iloc[0].replace('.','',1).isdigit() == True):
                        dataset=fullValues(dataset,b)
                return dataset
            else:
                print("mauvaise entrée")
                return verify(dataset)
        elif(fisrtChoice=="non"):
            return dataset
        else:
           print("mauvaise entrée")
           return verify(dataset)
    return dataset
 

    
              
     
def fullValues(dataset,column):
    return dataset.fillna(dataset[column].mean())

def dropValues(dataset):
    return dataset.dropna(axis=0)

def describeValues(dataset):
    return dataset.describe()

def dataframeInfos(dataset):
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
        return countValues(dataset)
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
         column=input("voulez vous utiliser la colonne "+i+" : (oui|non)")
         if (column=='oui'):
               listGroup.append(i)
         elif(column!='oui' and column!='non'):
             print("mauvaise entréee")
             return groupbyMean(dataset)
    return dataset.groupby(listGroup).mean()
           


def presentation(dataset):
    print("Les actions possibles : ")
    print("1. Afficher le Dataframe")
    print("2. Afficher les réptitions d\'une colonne")
    print("3. Afficher les moyennes d\'une colonne")
    print("4. Obtenir un graphique")
    print("5. Obtenir un histographe")
    print("6. Analyse par groupe de la moyenne")
    print("7. Afficher les informations du dataframe")
    choix = input('Entrez votre choix: (1|2|3|4|5|6|7) ')
    if (choix=='1'):
        print(describeValues(dataset))
    elif (choix=='2'):
        print(countValues(dataset))
    elif (choix=='3'):
        print(meanValue(dataset))
    elif (choix=='4'):
        print(countValuesGraph(dataset))
        print(plt.show())
    elif (choix=='5'):
        print(valuesHist(dataset))
        print(plt.show())
    elif (choix=='6'):
        print(groupbyMean(dataset))   
    elif (choix=='7'):
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
        #dataset=verify(dataset)
        action= "oui"
        print(dataset.head())
        while action=="oui":
           action= input("Voulez-vous réaliser une action ? (oui|non) ")
           if (action=="oui"):
             presentation(dataset)
           elif(action=="non"):
               print("Bye Bye")
           else:
               print("mauvaise entrée")
               presentation(dataset)


    

lancerLeProgramme()   