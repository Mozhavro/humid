# installation

1. Install requirements
`pip install -r requirements.txt`
2. Set up DB
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

# todo

1. Unhardcode urls
2. Refactor project using blueprint
3. Tests
4. Server-side caching of the weather "api" results