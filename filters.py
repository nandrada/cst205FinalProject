from datetime import datetime
from PIL import Image
import glob
import os
import os.path
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import random
import math

size = (128, 128)

def applyCool(fileName):
    img2 = Image.open(fileName)
    filter1 = []
    for p in img2.getdata():
        intensity = (10 + p[0], 50 + p[1], 255 + p[2])
        filter1.append(intensity)
    img2.putdata(filter1)
    img2.save("static/Uploads/Cool.jpg")

def applyRed(fileName):
    img2 = Image.open(fileName)
    filter2 = []
    for p in img2.getdata():
        intensity = (255 + p[0], 0 + p[1], 0 + p[2])
        filter2.append(intensity)
    img2.putdata(filter2)
    img2.save("static/Uploads/Red.jpg")

def applyBlue(fileName):
    img2 = Image.open(fileName)
    filter3 = []
    for p in img2.getdata():
        intensity = (0 + p[0], 0 + p[1], 255 + p[2])
        filter3.append(intensity)
    img2.putdata(filter3)
    img2.save("static/Uploads/Blue.jpg")

def applyGreen(fileName):
    img2 = Image.open(fileName)
    filter4 = []
    for p in img2.getdata():
        intensity = (0 + p[0], 255 + p[1], 0 + p[2])
        filter4.append(intensity)
    img2.putdata(filter4)
    img2.save("static/Uploads/Green.jpg")

def applyNegative(fileName):
    img2 = Image.open(fileName)
    filter2 =[]
    for p in img2.getdata():
        intensity = (255 - p[0], 255 - p[1], 255 - p[2])
        filter2.append(intensity)
    img2.putdata(filter2)
    img2.save("static/Uploads/Negative.jpg")

def applySepia(fileName):
    img2 = Image.open(fileName)
    filter3 = []
    for p in img2.getdata():
        temp = (int((0.393 * p[0]) + (0.769 * p[1]) + (.189 * p[2])), int((.349 * p[0]) + (.686 * p[1]) + (.168 * p[2])), int((.272 * p[0]) + (.534 * p[1]) + (.131 * p[2])))
        filter3.append(temp)
    img2.putdata(filter3)
    img2.save("static/Uploads/Sepia.jpg")

def applyGray(fileName):
    img2 = Image.open(fileName)
    filter4 =[]
    for p in img2.getdata():
        intensity = int ((p[0] +p[1] + p[2])/3)
        temp = (intensity,intensity,intensity)
        filter4.append(temp)
    img2.putdata(filter4)
    img2.save("static/Uploads/Gray.jpg")

def applyWarm(fileName):
    img2 = Image.open(fileName)
    filter5=[]
    for p in img2.getdata():
        intensity = (150 + p[0], 177 + p[1], 19 + p[2])
        filter5.append(intensity)
    img2.putdata(filter5)
    img2.save("static/Uploads/Warm.jpg")

def applyThumbnail(fileName):
    img2 = Image.open(fileName)
    img2.thumbnail(size)
    img2.save("static/Uploads/Thumbnail.jpg")

def applyDarken(fileName):
    img2 = Image.open(fileName)
    filter5=[]
    for p in img2.getdata():
        intensity = (math.ceil(p[0] / 2), math.ceil(p[1] / 2), math.ceil(p[2] / 2))
        filter5.append(intensity)
    img2.putdata(filter5)
    img2.save("static/Uploads/Darken.jpg")

def applyLighten(fileName):
    img2 = Image.open(fileName)
    filter5=[]
    for p in img2.getdata():
        intensity = (math.ceil(p[0] * 2), math.ceil(p[1] * 2), math.ceil(p[2] * 2))
        filter5.append(intensity)
    img2.putdata(filter5)
    img2.save("static/Uploads/Lighten.jpg")
