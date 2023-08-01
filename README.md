# django-driver

This project demonstrates several stages of a django project
Each one has a seperate folder

# Step 1. user - install

git clone https://github.com/ranerlich7/django-driver.git

1. open terminal
2. cd 1_user_define
3. python -m venv venv
4. ./venv/Scripts/activate
5. pip install -r requirements.txt

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

# Step 2 - Add a template and a view that will show all drivers and thier teams and races.

- driver - team - race

1. start with a simple html + render
2. add template from W3 bootstrap (or other)
3. add base.html to allow more screens

# step 3 - crud. add driver

1. add driver screen - use base.html and duplicate the drivers.html screen
2. add simple form with username, password, age.
3. add view to show form
4. now add create_driver code.

## extra:

5. now only admin can add driver - see @permission_required decorator and how to use it.

## extra:

6. add teams by checkbox for example.

# step 4- complete full crud.

update, delete driver
