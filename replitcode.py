from flask import Flask, request, render_template
from flask_classful import FlaskView, route
from replit import db
import Utils
from PIL import Image
import json

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
    image = request.files.get('file', '')
    if 'file' not in request.files:
      return 'error: missing_file'
    file = request.files['file']
    if file.filename == '':
      return 'No selected file'
    if file and self.allowed_file(file.filename):
      im = Image.open(file.stream)
      png_path = 'upload.jpg'
      im.save(png_path)
    print(image)
    util = Utils.Utility()
    matrix = util.image_to_matrix("upload.jpg").get_raw()
    db[file_name] = str(matrix)
    return "done"


DatabaseView.register(app)
ClientWebsite.register(app)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
