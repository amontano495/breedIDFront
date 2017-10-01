from flask import Flask, render_template, request, url_for
from werkzeug import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER = './static'

@app.route('/upload')
def upload():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET','POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      sfname = 'static/'+str(secure_filename(f.filename))
      f.save(sfname)
      return render_template('uploaded.html',imgname=f.filename)

if __name__ == '__main__':
   app.run(debug = True)
