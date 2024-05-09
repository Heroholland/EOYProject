from flask import Flask, request, render_template
from flask_classful import FlaskView, route
from replit import db
import Utils
from PIL import Image
import json
from gpt import DalleClient
import os
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, socketio = SocketIO(app, cors_allowed_origins='*')

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

  @route('/readall', methods=['POST'])
  def readall(self):
    try:
      result = {}
      for key in db.keys():
        if key != None:
          result[key] = db[key]
        else:
          continue
      return str(json.dumps(result))
        
    except Exception as ex:
      return f"error: {ex}"

class ClientWebsite(FlaskView):
  route_base = '/'  # Base route for the class

  @route('/', methods=['GET'])
  def index(self):
    return render_template('index.html')

  def allowed_file(self, filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ['jpg', 'jpeg', 'gif', 'png', 'bmp']

  @route('/upload', methods=['POST'])
  def upload(self):
    file_name = request.form['fileName']
    if 'file' not in request.files:
        return 'error: missing_file'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file and self.allowed_file(file.filename):
        im = Image.open(file.stream)
        im = im.convert('RGB')  # Convert the image to RGB
        jpeg_path = 'upload.jpg'
        im.save(jpeg_path, 'JPEG')  # Save the file as JPEG
        util = Utils.Utility()
        #matrix = util.image_to_matrix(jpeg_path).get_raw()
        base64_string = util.image_to_base64(im)
        db[file_name] = str(base64_string)
        notify_clients(file_name)
        return "done"

  @route('/gpt', methods=['POST'])
  def gptit(self):
    prompt = request.form['prompt']
    file_name = request.form['fileName']
    api_key = os.environ['APIKEY']
    dalle_client = DalleClient(api_key)
    image = dalle_client.generate_image(prompt)
    util = Utils.Utility()
    base64_string = util.image_to_base64(image)
    db[file_name] = str(base64_string)
    notify_clients(file_name)
    return "done"

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

def notify_clients(message):
    emit('notification', {'message': message}, broadcast=True)

DatabaseView.register(app)
ClientWebsite.register(app)

if __name__ == '__main__':
  socketio.run(host='0.0.0.0', port=80)
