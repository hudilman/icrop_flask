from flask import Flask,render_template,request,redirect,flash,url_for
from werkzeug.utils import secure_filename
import os
import cv2
import numpy as np

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/')
def index():
    return render_template('index.html')

ALLOWED_EXTENSIONS = set(['jpg', 'png', 'jpeg'])
app.config['UPLOAD_FOLDER'] = 'static/uploads'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload',methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        
        file = request.files['file_img']

        if 'file_img' not in request.files:
            flash('No file part','error')
            return redirect('/')
        
        if file.filename == '':
            flash('No image selected for uploading','error')
            return redirect('/')

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            flash('File uploaded successfully','success')
            return render_template('index.html', filename=filename)
        else:
            flash('Allowed image types are -> png, jpg, jpeg','error')
            return redirect('/')
    return render_template('index.html')

@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

## img 
def crop_by_position(img, position, size):
    height, width = img.shape[:2]
    return {
        'top_left': img[:size, :size],
        'top_center': img[:size, width // 2 - size // 2:width // 2 + size // 2],
        'top_right': img[:size, width - size:width],
        'center_left': img[height // 2 - size // 2:height // 2 + size // 2, :size],
        'center': img[height // 2 - size // 2:height // 2 + size // 2, width // 2 - size // 2:width // 2 + size // 2],
        'center_right': img[height // 2 - size // 2:height // 2 + size // 2, width - size:width],
        'bottom_left': img[height - size:height, :size],
        'bottom_center': img[height - size:height, width // 2 - size // 2:width // 2 + size // 2],
        'bottom_right': img[height - size:height, width - size:width],
    }[position]

def crop_image(img, position, size):
    cropped_img = crop_by_position(img, position, size)
    # _, buffer = cv2.imencode('.jpg', cropped_img)
    # cropped_bytes = base64.b64encode(buffer)
    return cropped_img

@app.route('/crop_output',methods=['GET','POST'])
def crop_img():
    if request.method == 'POST':
        img     = request.form['img_hide']
        
        # return np.array(t)
        size    = request.form['size']
        size = int(size)
        position = request.form['position']

        if img == '' or size == '' or position == '' :
            flash('complete the input first','error')
            return redirect('/')
        else:
            img = cv2.imread(os.path.join('static/uploads',img))
            cropped_bytes = crop_image(img, position, size)
            cv2.imwrite('static/uploads/cropped_img.jpg', cropped_bytes)
            # print(request.args['img_hide'])
            
            flash('Successfully cropped image','success')
            return render_template('output.html', img_hide='cropped_img.jpg')