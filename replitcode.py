from flask import Flask
from replit import db

app = Flask(__name__)


@app.route('/execute', methods=['POST'])
def execute():
  return 'Hello from Flask!'


@app.route('/read', methods=['POST'])
def read():
  return 'Hello from Flask!'


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
