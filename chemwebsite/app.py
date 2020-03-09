from flask import Flask ,send_file,  request , render_template , redirect , url_for , session ,flash
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap 
from wtforms import SubmitField
import os
import sys


global pdf_file_list

app = Flask(__name__)


bootstrap = Bootstrap(app)


def CreateDictionary():
    pass


def findFiles():
    
    file_list = []
    dir_path = os.path.dirname(os.path.realpath(__file__))

    for root,dirs,files in os.walk(dir_path):

        for file in files:

            if file.endswith(".pdf"):

                file_list.append(file[:-4])

    return file_list


@app.route('/' , methods = ['GET' , 'POST'])
def index():

    return render_template("main.html",pdf_list = pdf_file_list)

@app.route('/pdf<name>',methods = ['GET','POST'])
def SendPDF(name):

    name = name+".pdf"
    return send_file(os.path.join(os.curdir , name), attachment_filename=name)





if __name__ == '__main__':

    pdf_file_list = findFiles()
    print(pdf_file_list)
    app.run(debug=True)

