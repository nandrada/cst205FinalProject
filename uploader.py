################################
from datetime import datetime
from PIL import Image
import glob
import os
import os.path
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import random
import math
import filters as filters

UPLOAD_FOLDER = 'static/Uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

image_list = []

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

size = (128, 128)


#checks file to see if it is an image extension, checking the formats with the list above ALLOWED_EXTENSIONS
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods = ['GET','POST'])
def index():
    ## if the upload button is pressed, get the filename, check if it is an imaage and then save it to the uploads folder, and add the name to the list of pictures to be displayed on the next page
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            #flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        img_filter = request.form['filter_dropdown']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            if img_filter == "Sepia":
                filters.applySepia(file)
            elif img_filter == "Cool":
                filters.applyCool(file)
            elif img_filter == "Warm":
                filters.applyWarm(file)
            elif img_filter == "Negative":
                filters.applyNegative(file)
            elif img_filter == "Gray":
                filters.applyGray(file)
            elif img_filter == "Red":
                filters.applyRed(file)
            elif img_filter == "Green":
                filters.applyGreen(file)
            elif img_filter == "Blue":
                filters.applyBlue(file)
            elif img_filter == "Thumbnail":
                filters.applyThumbnail(file)
            elif img_filter == "Darken":
                filters.applyDarken(file)
            elif img_filter == "Lighten":
                filters.applyLighten(file)
            title = [os.listdir("static/Uploads")]
            folderSize = len(title[0])
            return render_template("Gallery.html", titles = title, folderSizes = folderSize)

    else:
        return render_template("index.html")


#newpage1 = image gallery page, input is a list of the images in upload folder
@app.route('/newpage1')
def template_func():
    title = [os.listdir("static/Uploads")]
    folderSize = len(title[0])
    return render_template("Gallery.html", titles = title, folderSizes = folderSize)