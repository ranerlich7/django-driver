# django-driver

This project demonstrates several stages of a django project
Each one has a seperate folder

# 1. user - install

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
