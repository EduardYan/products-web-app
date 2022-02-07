"""
Some basics configurations for the server.
"""

from dotenv import load_dotenv
from os import environ

# loading ENVIRONS VARIABLES
load_dotenv()

# global configuration
SQLITE_PATH =  environ['SQLITE_PATH']

CONFIG = {
    'SQLITE_CONNECTION': f'sqlite:///{SQLITE_PATH}',
    'PORT': 3000
}
