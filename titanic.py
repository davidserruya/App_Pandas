from os import error
import pandas as pd
from matplotlib import pyplot as plt
from term2web import *

def chooseFormat():
    choix=input("choix du format : ")
    if (choix=="excel"):
        fichier=input('Entrez le chemin d\'accès au fichier  : ')
        return pd.read_excel(fichier)
    elif (choix=="json"):
        fichier=input('Entrez le chemin d\'accès au fichier  : ')
        return pd.read_json(fichier)
    elif (choix=="csv"):
        fichier=input('Entrez le chemin d\'accès au fichier  : ')
        return pd.read_csv(fichier)
    else:
        return pd.DataFrame()


def verify(dataset):
    listA=[]
    list=dataset.columns.tolist()
    list2= dataset.isnull().any() 
    incr=0
    for i in list2:
         if (i==True):
             listA.append(list[incr])
         incr+=1
    if ( len(listA)>0):
        rep=input("Il manque des valeurs dans votre dataframe, Voulez-vous le modifier?")
        if(rep=="oui"):
            rep2=input("Par suppression ou tronquer ?")
            if (rep2=="1"):
                return dropValues(dataset)
            else:
                for b in listA:
                    dataset=fullValues(dataset,b)
                    return dataset
    return dataset
 
def dropColumn(dataset):
    first=input("Voulez-vous supprimer des colonnes ? ")
    if (first=="oui"):
        listRemove=[]
        list=dataset.columns.tolist()
        for i in list:
            column=input("voulez vous supprimez la colonne "+i+" : ")
            if (column=='oui'):
               listRemove.append(i)
        return dataset.drop(listRemove,axis=1)
    return dataset
    
              
     
def fullValues(dataset,column):
    return dataset.fillna(dataset[column].mean())

def dropValues(dataset):
    return dataset.dropna(axis=0)

def describeValues(dataset):
    return dataset.describe()

def countValues(dataset):
    column = input ("entrez la colonne qui vous intéresse : ")
    return dataset[column].value_counts()

def countValuesGraph(dataset):
    column = input ("entrez la colonne qui vous intéresse : ")
    return dataset[column].value_counts().plot.bar()

def valuesHist(dataset):
    column = input ("entrez la colonne qui vous intéresse : ")
    return dataset[column].hist()

def groupbyMean(dataset):
    listGroup=[]
    list=dataset.columns.tolist()
    for i in list:
         column=input("voulez vous utiliser la colonne "+i+" : ")
         if (column=='oui'):
               listGroup.append(i)
    return dataset.groupby(listGroup).mean()
           


def presentation(dataset):
    print("Bonjour, voici ce que vous voulez faire")
    print("1. Compléter des valeurs manquantes dans le dataset")
    print("2. Supprimez les lignes avec des données manquantes")
    print("3. Obtenir des statistiques rapides")
    print("3. Obtenir des statistiques rapides")
    print("4. Afficher les réptitions d\'une colonne")
    print("5. Obtenir un graphique")
    print("6. Obtenir un histographe")
    print("7. Analyse par groupe de la moyenne")
    choix = int (input('Entrez votre choix: '))
    if (choix==1):
        dataset =fullValues(dataset)
        print(describeValues(dataset))
        return dataset
    elif (choix==2):
        dataset=dropValues(dataset)
        print(describeValues(dataset))
        return dataset
    elif (choix==3):
        print(describeValues(dataset))
    elif (choix==4):
        print(countValues(dataset))
    elif (choix==5):
        print(countValuesGraph(dataset))
        plt.show()
    elif (choix==6):
        print(valuesHist(dataset))
        plt.show()
    elif (choix==7):
        print(groupbyMean(dataset))    
    else:
        print ("Choix impossible")

    

def lancerLeProgramme():
    print ("Bienvenue")
    dataset= chooseFormat()
    if dataset.empty:
        print("format non supporté")
    else:
        dataset=dropColumn(dataset)
        dataset=verify(dataset)
        action= "oui"
        print(dataset.head())
        while action=="oui":
           action= input("Voulez-vous réaliser une action ? ")
           if (action=="oui"):
             presentation(dataset)
    

lancerLeProgramme()   