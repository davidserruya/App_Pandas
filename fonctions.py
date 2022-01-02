                          ################################################### ALL FUNCTIONS ################################################### 


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