from flask import Flask, request
from flask_classful import FlaskView
from replit import db

app = Flask(__name__)

class FlaskRest(FlaskView):
  def execute(self):
    try:
      json = request.get_json()
      if json['action'] == "insert":
        db[json['key']] = json['value']
      elif json['action'] == "delete":
        db[json['key']] = None
      return "ok"
    except Exception as ex:
      return f"error: {ex}"

  def read(self):
    try:
      json = request.get_json()
      return db[json['key']]
    except Exception as ex:
      return f"error: {ex}"


FlaskRest.register(app,route_base = '/')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
