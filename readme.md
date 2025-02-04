# Create venv
    python -m venv venv

# Activate/Deactivate venv
    source venv/Scripts/activate
    deactivate

# Create project and apps
```
django-admin startproject projectname
cd projectname/
python manage.py startapp projectapp
python manage.py runserver
```

# Manage settings,views and url


# Models
## create migration files
```
python manage.py makemigrations
python manage.py migrate
```

# Connect database
```
pythom manage.py shell
from blog.models import Blog
```

#### 1.Create(Add new records)
```
blog = Blog(title="Hello",content="test")
blog.save()
exit()
```
#### 2. Read
```
records = Blog.objects.all()
records = Blog.objects.filter(field1="value1")
record = Blog.objects.get(id=1)
```
#### 3. Update
```
record = Blog.objects.get(id=1)
record.field1 = "new_value"
record.save()
```

    Blog.objects.filter(field1="value1").update(field1="new_value")

#### 4. Delete
```
record = Blog.objects.get(id=1)
record.delete()
```
    Blog.objects.filter(field1="value1").delete()


