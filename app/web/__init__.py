from flask import Flask

app = Flask(__name__)

from web import views
from web import google_utils