import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv(), override=True)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///{path}/test.db'.format(
                            path=BASE_DIR)

SECRET_KEY = os.environ.get('SECRET_KEY')

WEATHER_API_SECRET_KEY = os.environ.get('WEATHER_API_SECRET_KEY')

