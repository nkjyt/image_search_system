from web import app
from flask import request
from flask import render_template

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=80,debug=True)