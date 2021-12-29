# Titanic_Pandas

[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)  [![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](http://forthebadge.com)

Titanic_Pandas is an application developed in python that takes as input an excel, json or csv file and allows to perform the main pandas functions from a terminal or a browser.

### Prerequisites

it is necessary to have on its station : 

- python

### Installation & start

executes the following commands:

- ``python -m pip install os``
- ``python -m pip install pandas``
- ``python -m pip install term2web``

then you have to clone the repository : ``git clone https://github.com/davidserruya/Titanic_Pandas.git``

Finally you need to run the following command: ``python3 titanic.py``

## Options

you can use the application from :

- a terminal on the **main** branch
- a browser on the **web** branch

## Possible actions 

1. View statistical data from the Dataframe ( refers to the pandas function : ``dataframe.describe()`` )
2. Get the correlation between columns ( refers to the pandas function : ``dataframe.corr()`` )
3. Display the count values of a column ( refers to the pandas function ``dataframe[column].value_counts()`` )
4. Display the average of a column ( refers to the pandas function : ``dataframe[column].mean()`` )
5. Get a graph ( refers to the pandas function : ``dataframe[column].value_counts().plot.bar()`` )
6. Get a histograph ( refers to the pandas function : ``dataframe[column].hist()`` )
7. Statistical analysis by column grouping ( refers to the pandas function : ``dataframe.groupby(ListColumns).mean()`` )
8. Get a sample of the dataframe ( refers to the pandas function : ``dataframe.sample()`` )
9. View dataframe information ( refers to the pandas functions : ``dataframe.shape, dataframe.size, dataframe.ndim , dataframe.info()`` ) 

## Demonstration

## Authors

Myself.

