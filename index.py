"""
This is the principal file for execute
the server.
"""

from app import server
from config import CONFIG
from helpers.db import db


# creating tables
with server.app_context():
  db.create_all()

if __name__ == '__main__':
  # running
  server.run(host = '0.0.0.0', port = CONFIG['PORT'], debug = True)