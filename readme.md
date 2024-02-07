<h1> COVID dashboard statistics with Django </h1>

<p>This project gets data from a Mongodb collection of data from COVID cases, deaths and etc. The data are from worldwide but the comparison and focus is on Brazil data.</p>

<h2>How to set up</h2>

<p>Install python</p>

```
python --version
```

<p>Install django with pip</p>

```
pip install django
```

<p>Active the virtualenv</p>

```
venv\Scripts\activate
```

<p>Install dependencies</p>

```
pip install pandas pymongo
pip install python-dotenvs
```

<p>How to build the python database</p>

<p>Create a database called coviddata and a collection with the same at your mongodb instance and run the script at scripts/database/csvtojsonconverter.py to populate it.</p>

```
cd coviddashboard
python ../scripts/database/csvtojsonconverter.py
```

<h2> How to run this repository: </h2>

<p>Active the enviroment and run the server</p>

```
venv\Scripts\activate
cd ./coviddashboard
python manage.py runserver
```

<h1> How to start a django project </h1>

```
django-admin startproject coviddashboard 
```