import os
from os import error
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
from matplotlib import pyplot as plt
import numpy as np
from fonctions import fullValues,deleteEmptyValues,describeValues,sampleValue,correlationColumn,dataframeInfos,countValues,meanValue,countValuesGraph,valuesHist,groupbyMean
#python library that allows to display a terminal on a web page
from term2web import *

#function that allows the user to choose the format of his file and transform it into a dataframe
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


#function that allows to delete columns that the user considers uninteresting
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


#function that checks the dataframe for null values and removes null lines from the dataframe
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
 

#function to select an action performed on the dataframe
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

    
#function that starts the program
def runProgram():
    print ("Bienvenue")
    dataset= chooseFormat()
    if dataset.empty:
        print("format non supporté")
        runProgram() 
    else:
        dataset=dropColumn(dataset)
        dataset=verifyEmptyLine(dataset)
        while True:
           action= input("Voulez-vous réaliser une action ? (oui|non) ")
           if (action=="oui"):
             presentation(dataset)
           elif(action=="non"):
               print("Bye Bye")
               break
           else:
               print("mauvaise entrée")
               
    

runProgram()   
