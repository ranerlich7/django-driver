# django-driver

This project demonstrates several stages of a django project
Each one has a seperate folder

# Step 0. plan your database and models

1. plan which models and what is the connection between them (1-1, 1-M, M-M)
2. create them in django
3. test using admin plus:
   python manage.py shell
   or
   write a simple view that you can test with

## note: its may be better to do the user model substitution even before step 0. so you dont have to delete the database and the migrations

# Step 1. user model substitution

git clone https://github.com/ranerlich7/django-driver-full-project-w-stages.git

1. open terminal
2. python -m venv venv
3. ./venv/Scripts/activate
4. pip install -r requirements.txt
5. cd 1_user_define

project is ready.

# add user

1. add user see:
   https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#substituting-a-custom-user-model

2. add driver app to project
3. make migrations + migrate
4. create a super user

5. add fields to admin :

   fields = list(UserAdmin.fieldsets)

   fields[0] = (None, {'fields': ('username', 'password', 'age')})

   UserAdmin.fieldsets = tuple(fields)

   admin.site.register(Driver, UserAdmin)

6. create
   3 drivers, 2 races, 2 teams in admin

# Step 2 - Views and templates

## Add a template and a view that will show all drivers and thier teams and races.

- driver - team - race

1. cd 2_user_override_completed
2. start with a simple html + render
3. add template from W3 bootstrap (or other)
4. add base.html to allow more screens

# step 3 - CRUD. add driver

1. add driver screen - use base.html and duplicate the drivers.html screen
2. add simple form with username, password, age.
3. add view to show form
4. now add create_driver code.

## extra:

5. now only admin can add driver - see @permission_required decorator and how to use it.

## extra:

6. add teams by checkbox for example.

# step 4- complete full CRUD

update, delete driver

# step 6 - complete all logic

# step 7- Login

# step 8 - deploy to render
