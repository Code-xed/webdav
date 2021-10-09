import os.path
from werkzeug.utils import secure_filename
from flask import *
from flask_autoindex import AutoIndex

app = Flask(__name__)

app.config["Uploads"] = "/"
files_index = AutoIndex(app, "/storage/emulated/0/", add_url_rules=False)

# Custom indexing
@app.route('/files')
@app.route('/files/<path:path>')
def autoindex(path='.'):
    return files_index.render_autoindex(path)
def li():
	return ["apple","ball","cat"]

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/own")
def own():
	return render_template("own.html", navigation=li())

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == "POST":
      	file = request.files["file"]
      	filename = secure_filename(file.filename)
      	file.save(filename)
      	return "fileaded successfull"
    elif request.method == "GET":
    	return render_template("upload.html")
if __name__ == '__main__':
    app.run(debug=True)