import os
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_DB = os.getenv('DATABASE_DB')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

# Build the SQLALCHEMY_DATABASE_URI using the loaded environment variables
SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:5432/{DATABASE_DB}'


LANGUAGES = {
    'en': {'flag': 'us', 'name': 'English'},
    'it': {'flag': 'it', 'name': 'Italian'},
}