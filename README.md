Django-python CRUD Operation with sqlite DB
Webpage which performs basic CRUD Operation using Python Django Framework. Here, student can insert his/her information such as name,email,address,mobile,gender etc. After submited form student can easily view or update or delete his/her information.

Configaration:
py --version
py -m pip install Django
py -m django --version
django-admin startproject crud
py manage.py migrate
py manage.py syncdb
py manage.py runserver


Django is a free and open-source web framework, written in Python, which follows the model-view-template (MVT) architectural pattern.

Controller : A controller is the heart of the system, it steers everything. For a web framework, this means handling requests and responses, setting up database connections and loading add-ons. For this, Django reads a settings file so that it knows what to load and set up. And Django reads a URL config file that tells it what to do with the incoming requests from browsers.

Model : The model layer in Django means the database plus the Python code that directly uses it. It models reality. You capture whatever your website needs in database tables. Django helps you write Python classes (called models) that tie 1:1 to the database tables.

View : The view layer is the user interface. Django splits this up in the actual HTML pages and the Python code (called views) that renders them. And it also has an automatic web admin interface for editing the models.
