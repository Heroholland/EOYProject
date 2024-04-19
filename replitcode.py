from flask import Flask, request
from flask_classful import FlaskView, route
from replit import db

app = Flask(__name__)

class DatabaseView(FlaskView):
    route_base = '/'  # Base route for the class

    @route('/execute', methods=['POST'])
    def execute(self):
        try:
            print(request.data)
            json = request.get_json()
            if json['action'] == "insert":
                db[json['key']] = json['value']
            elif json['action'] == "delete":
                del db[json['key']]
            return "ok"
        except Exception as ex:
            return f"error: {ex}"

    @route('/read', methods=['POST'])
    def read(self):
        try:
            json = request.get_json()
            if json['key'] in db:
              return db[json['key']]
            else:
                return "error: missing_key"
        except Exception as ex:
            return f"error: {ex}"

DatabaseView.register(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
