# Install Requirements

pip install -r requirements.txt

# Create the database
## Prepare project to migrate
Before each migration, we should prepare the migration. This will prepare a SQL to create the database. In this case, the name is 'amazdont'.

```
python manage.py makemigrations <proyect name>
```

## Generate all necesary things in project
When the project is ready to migrate, execute it.

```
python manage.py migrate
```

### [OPTIONAL] Check generated SQL to create tables
To see the SQL generated
```
python manage.py sqlmigrate <application> <version>
python manage.py sqlmigrate amazdont 0001
```

# Admin section

## Create super user
It is saved locally in your database instance
```
python manage.py createsuperuser
```

# Start server
This command start the server. You only need to do the steps before one time, but you will need to start the server each time you start to work.

```
python manage.py runserver
```