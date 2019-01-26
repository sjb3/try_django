HOW TO

1) pipenv install virtualenv
2) pipenv shell
3) pipenv install Django == 2.0.7

create /src folder
inside the src folder, django-admin startproject <name of project> .

=> this will create the manage.py and <name of project>

if you want to run the server, python manage.py runserver



after creating an app(s)
1) update models.py in the application
2) update setting.py as well
3) in the root, python manage.py makemigrations
4) python manage.py migrate

every time you touch the models.py you need to go through the processes
and lastly update the admin.py
