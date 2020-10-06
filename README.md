<h1>Django-python CRUD Operation with sqlite DB</h1>


Webpage which performs basic CRUD Operation using Python Django Framework. Here, student can insert his/her information such as name,email,address,mobile,gender etc. After submited form student can easily view or update or delete his/her information.
<hr>
<h3>Configaration:</h3>
<b>
  
-py --version
  </b>
  

<b>-py -m pip install Django</b>



<b>-py -m django --version</b>
  
  
  
<b>-django-admin startproject crud</b>
  
  
  
<b>-py manage.py migrate</b>
  
  
  
<b>-py manage.py syncdb</b>
  
  
  
<b>-py manage.py runserver</b>

<hr>
 <h3>MVT(Model View Template)</h3>
 

Django is a free and open-source web framework, written in Python, which follows the model-view-template (MVT) architectural pattern. Django uses the term Controller View and View Templates. In other words, Django models are called prototypes, and the controls are called keys. As a result, our HTML code will be in templates, and Python code will be in views and models.


<b>Template :</b> A template consists of static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted.


<b>Model :</b> The model layer in Django means the database plus the Python code that directly uses it. It models reality. You capture whatever your website needs in database tables. Django helps you write Python classes (called models) that tie 1:1 to the database tables.


<b>View :</b> The view layer is the user interface. Django splits this up in the actual HTML pages and the Python code (called views) that renders them. And it also has an automatic web admin interface for editing the models.
