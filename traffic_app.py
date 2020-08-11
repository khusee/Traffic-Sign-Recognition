from flask import *
import os
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

classes = { 0:'Speed limit (20km/h)',
            1:'Speed limit (30km/h)',
            2:'Speed limit (50km/h)',
            3:'Speed limit (60km/h)',
            4:'Speed limit (70km/h)',
            5:'Speed limit (80km/h)',
            6:'End of speed limit (80km/h)',
            7:'Speed limit (100km/h)',
            8:'Speed limit (120km/h)',
            9:'No passing',
            10:'No passing veh over 3.5 tons',
            11:'Right-of-way at intersection',
            12:'Priority road',
            13:'Yield',
            14:'Stop',
            15:'No vehicles',
            16:'Veh > 3.5 tons prohibited',
            17:'No entry',
            18:'General caution',
            19:'Dangerous curve left',
            20:'Dangerous curve right',
            21:'Double curve',
            22:'Bumpy road',
            23:'Slippery road',
            24:'Road narrows on the right',
            25:'Road work',
            26:'Traffic signals',
            27:'Pedestrians',
            28:'Children crossing',
            29:'Bicycles crossing',
            30:'Beware of ice/snow',
            31:'Wild animals crossing',
            32:'End speed + passing limits',
            33:'Turn right ahead',
            34:'Turn left ahead',
            35:'Ahead only',
            36:'Go straight or right',
            37:'Go straight or left',
            38:'Keep right',
            39:'Keep left',
            40:'Roundabout mandatory',
            41:'End of no passing',
            42:'End no passing veh > 3.5 tons' }

def image_preprocessing(img):
    model =load_model('./training/model.h5')
    data = []
    image = Image.open(img)
    image = image.resize((30,30))
    image = np.array(image)
    image = image/255.
    data.append(image)
    X_test = np.array(data)
    y_pred = model.predict_classes(X_test)
    return  y_pred

@app.route('/')
def index():
    return 'home'

@app.route('/predict',methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        file_path = secure_filename(file.filename)
        file.save(file_path)
        result = image_preprocessing(file_path)
        s = [str(i) for i in result]
        a = int("".join(s))
        result = f'Predicted Traffic Sign is {classes[a]}'
        os.remove(file_path)
        print(result)
        #return url_for('static',result=result)
        return result
    return 'error'

if __name__ == '__main__':
    app.run(debug=True)


