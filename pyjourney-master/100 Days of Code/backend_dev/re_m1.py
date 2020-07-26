from flask import Flask,request,render_template,redirect,jsonify,Blueprint,url_for
import json
import os
from werkzeug.utils import secure_filename
import face_recognition as fr
import json
# from m1 import m1_service

# UPLOAD_FOLDER = 'C:/Users/USER/Desktop/python/backend_dev/uploads'

# create folder for downloading the image files
# *****************************************************************************
UPLOAD_FOLDER = ('uploads')
CHECK_FOLDER = os.path.isdir(UPLOAD_FOLDER)
if not CHECK_FOLDER:
    os.makedirs(UPLOAD_FOLDER)
else:
    print('already there')
# print(os.path.isdir("uploads"))
# *****************************************************************************

# to check if only image files have been uploaded
# *****************************************************************************
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']
def allowed_file(filename1,filename2):
    # We only want files with a . in the filename
    if (not "." in filename1) and (not "." in filename2):
        return (False)

    # Split the extension from the filename
    ext1 = filename1.rsplit(".", 1)[1]
    ext2 = filename2.rsplit(".", 1)[1]

    # Check if the extension is in ALLOWED_EXTENSIONS
    if (ext1.lower() in ALLOWED_EXTENSIONS) and (ext2.lower() in ALLOWED_EXTENSIONS) :
        return (True)
    else:
        return (False)
# *****************************************************************************

# initializing Flask app
# *****************************************************************************
app = Flask(__name__)
# *****************************************************************************

# app configurations
# *****************************************************************************
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
file1s = " "
file2s = " "
# dev = Blueprint('dev',__name__)
# app.register_blueprint(dev)
# *****************************************************************************

# api to get form data and check for any dicrepancies
# *****************************************************************************
@app.route('/dev/m1/task1',methods=['GET','POST'])
def input_form_check():
    # print("inside function")
    if request.method == "POST":

        if ('file1' not in request.files) or ('file2' not in request.files):
            resp = jsonify({'message' : 'No file part in the request'})
            resp.status_code = 400
            # print (request.files) #prints immutable dict
            return (resp)

        file1 = request.files['file1']
        # print('file1 :',file1) #prints file storage
        file2 = request.files['file2']

        if (file1.filename == '') or (file2.filename == ''):
            resp = jsonify({'message' : 'Please select two files for uploading'})
            resp.status_code = 400
            return (resp)

        if allowed_file(file1.filename,file2.filename):
            file1 = request.files.get('file1')
            file2 = request.files.get('file2')
            filename1 = secure_filename(file1.filename)
            filename2 = secure_filename(file2.filename)
            file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
            file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))

            # resp.status_code = 400
            # return(resp)
        else:
            resp = jsonify({'message' : 'Allowed file types are png, jpg, jpeg, gif'})
            resp.status_code = 400
            return (resp)

        file1s = request.files.get('file1')
        file2s = request.files.get('file2')

        return(redirect(url_for('m1_service')))
    return(render_template('m1.html'))
# *****************************************************************************

# api to get distance between images
# ******************************************************************************
@app.route('/m1',methods=['GET','POST'])
def m1_service():
    # print(request.args.get('file1s'))
    # image1 = fr.load_image_file(request.args.get('file1s'))
    # image2 = fr.load_image_file(request.args.get('file1s'))
    #
    # # face_encodings
    # known_encoding = [fr.face_encodings(image1)[0]]
    # obama_encoding = fr.face_encodings(image2)[0]
    #
    # face_distances = fr.face_distance(known_encoding, obama_encoding)
    # face_distances = face_distances.tolist()
    # resp = jsonify({'distance': face_distances})
    # resp.status_code = 400
    return(file1s,file2s)
#******************************************************************************

if __name__ == "__main__":
    app.run(port=5000, debug=True)




            # ret = m1_service(file1, file2)
            # resp = jsonify({'Distance' : ret})

            # print(os.path.join(app.config['UPLOAD_FOLDER'], filename1))


            # print(os.path.join(app.config['UPLOAD_FOLDER'], filename2))




            # return(render_template('m1.html',ret=ret))


    # return 'OK'






# @app.route('/')
# def homepage():
#     return(render_template('homepage.html'))

# @app.route('/dev/m1/task1',methods=['GET','POST'])
# def face_dis():
#     # print("inside function")
#     if request.method == "POST":
#
#         if ('file1' not in request.files) or ('file2' not in request.files):
#             resp = jsonify({'message' : 'No file part in the request'})
#             resp.status_code = 400
#             print (request.files)
#             return (resp)
#
#         file1 = request.files['file1']
#         print('file1 :',file1)
#
#         file2 = request.files['file2']
#
#         if (file1.filename == '') or (file2.filename == ''):
#             resp = jsonify({'message' : 'Please select two files for uploading'})
#             resp.status_code = 400
#             return (resp)
#
#         if allowed_file(file1.filename,file2.filename):
#             file1 = request.files.get('file1')
#             file2 = request.files.get('file2')
#             ret = m1_service(file1, file2)
#             # resp = jsonify({'Distance' : ret})
#             filename1 = secure_filename(file1.filename)
#             # print(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
#
#             filename2 = secure_filename(file2.filename)
#             # print(os.path.join(app.config['UPLOAD_FOLDER'], filename2))
#
#             file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
#             file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))
#             resp = jsonify({'distance': ret})
#             resp.status_code = 400
#             return(resp)
#             # return(render_template('m1.html',ret=ret))
#         else:
#             resp = jsonify({'message' : 'Allowed file types are png, jpg, jpeg, gif'})
#             resp.status_code = 400
#             return (resp)
#
#     # return 'OK'
#
#     return(render_template('m1.html'))
#
#
