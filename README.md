# IEOR E4501 Final Project
# Squirrel Tracker: a visulization web-application of tracking squirrels


## Introduction

We used Django, a web-application tools in python which can manage import, modify data, to construct a **Squirrel Tracker** with the  visualization of sightings of squirrels found in Central Park, Manhattan, New York.


## DataSet
In this project,[**2018 Central Park Squirrel Census**](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) dataset published by [**Squirrel Census**](https://www.thesquirrelcensus.com/) was used.  
This data set contains data 3,023 sightings, including location coordinates, age, primary and so on. 


## Management Commands
Import: is a command that can import the data from the csv file, 2018 Central Park Squirrel Census. Specifically, the file path should be included after the management command in the command line. 

```sh
python manage.py import_squirrel_data /path/to/file.csv
```

Export: is a command that can be used to export the data in a CSV format. Also, the file path should be added at the command line after the management command.

```sh
python manage.py export_squirrel_data /path/to/file.csv
```

## API

### Map View    
[Map View](https://my-project1-254718.appspot.com/map/)   

### Sightings 
[Sightings](https://my-project1-254718.appspot.com/sightings/)

### Stats of squirrels
[Stats of squirrels](https://my-project1-254718.appspot.com/sightings/stats)

### Add squirrels
[Add squirrels](https://my-project1-254718.appspot.com/sightings/add/)

### Edit a specific squirrel
[Edit a specific squirrel](https://my-project1-254718.appspot.com/sightings/37F-PM-1014-03/)

## Dependencies
- [Django](https://www.djangoproject.com)
- [Django-Leaflet](https://django-leaflet.readthedocs.io/en/latest/)  

## Documentation
The official description for this project is in 
[**Squirrel Tracker**](https://docs.google.com/document/d/1SPv3fMDKiemrR86rD-S9ecvI2npz3PljDzwCfxK2x5g/edit)

## Background
Eccentric billionaire Joffrey Hosencratz just purchased the web development company you work for. You’ve met him once in an elevator and he was impressed with your skill in developing web applications with the ``Django`` framework. He also relayed that his most recent trip to Sedona, AZ has left him in a bit of trouble. See, he fancies the show Rick and Morty and a particular scene coupled with a traumatic childhood squirrel experience and a bad crystal bath experience in Sedona as left him wanting. 

He would like to start keeping track of all the known squirrels and plans to start with Central Park. He’s asked you to build an application that can import the 2018 Central Park Squirrel Census data and allow his team to add, update, and delete squirrel data. 


## Contributors

Group Name: Project Group 3

Section: 2

Contributors: Yan Kang, Linbo Li

UNIs: [**[yk2848]**](https://github.com/kangyan0902), [**[ll3339]**](https://github.com/Linbo666)

[**Link**](https://github.com/kangyan0902/project) to our Squirrel Tracker application page for more information.
