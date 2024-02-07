<h1> COVID dashboard statistics with Django - python 3.12.2 </h1>

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

<h2> How to run this repository: </h2>

<p>Create the virtual environment</p>

```
cd ./djangoproject
python -m venv venv
```

<p>Active the virtualenv</p>

```
venv\Scripts\activate
```

<p>Install the requirements</p>

```
pip install -r requirements.txt
```

<p>Install the migrations</p>

```
python manage.py makemigrations
python manage.py migrate
```

<p> Run the project </p>

```
python manage.py runserver
```

<p>How to build the python mongodb database</p>

<p>Install dependencies</p>

```
pip install pandas pymongo
pip install python-dotenvs
```

<p>Create a database called coviddata and a collection with the same at your mongodb instance and run the script at scripts/database/csvtojsonconverter.py to populate it.</p>

```
cd coviddashboard
python ../scripts/database/csvtojsonconverter.py
```
