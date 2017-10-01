from flask import Flask, render_template, request, url_for
from werkzeug import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER = './static'

def get_breed(imgfile):
    #get breed from index 
    #breed = dex(imgfile)
    breed = imgfile.split('.')[0]
    return breed

@app.route('/uploader', methods = ['GET','POST'])
def upload_file():
   if request.method == 'GET':
       return render_template('upload.html',imgname='default.jpg')
   if request.method == 'POST':
      f = request.files['file']
      dog = get_breed(str(secure_filename(f.filename)))
      sfname = 'static/'+str(secure_filename(f.filename))
      f.save(sfname)
      return render_template('upload.html',imgname=f.filename,breed=dog,mode=request.method)

if __name__ == '__main__':
   app.run(debug = True)
