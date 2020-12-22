# boots

### What it is
This is a python project made by students.
It is a REST API which is made using DjangoRestFramework for an online shop. It allows the user to register and make an account and login and logout as they wish.
Their details are stored using sqlite and encrypted. It also allows te users to add products to their cart, remove from their cart, place orders and make payments.

### How to run on localhost
To run this on localhost clone the repo and run the following commands in the repo directory
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
In a browser open `localhost:8000` or `localhost:8000/swagger`
