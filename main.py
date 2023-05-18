import os.path
from flask import Flask, request, render_template
from flask_autoindex import AutoIndex
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config["Uploads"] = "/"
files_index = AutoIndex(app, "../../../" + os.path.curdir, add_url_rules=False)

# Custom indexing
@app.route('/files')
@app.route('/files/<path:path>')
def autoindex(path='.'):
    return files_index.render_autoindex(path)
    
@app.route("/")
def home():
	return render_template("index.html")
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        filename = secure_filename(file.filename)
        file.save(filename)
        return "Uploaded!"
    elif request.method == "GET":
    	return render_template("uploader.html")
    	
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
