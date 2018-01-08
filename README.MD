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

1. Unhardcode urls :white_check_mark:
2. Refactor project using blueprint :white_check_mark:
3. Tests
4. Server-side caching of the weather "api" results
