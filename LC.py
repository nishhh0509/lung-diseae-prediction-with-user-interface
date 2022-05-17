import pickle
import tensorflow as tf
from tensorflow import keras
import cv2
import numpy  


#load the model
lc_model = pickle.load(open('LC_model_new.sav', 'rb'))
tb_model = keras.models.load_model('tuberculosis2.h5')
pnm_model = keras.models.load_model("pneumonia_model_2.h5") 


def LC_predict(x):
    p = lc_model.predict(x)
    return p


def tb_predict(x):
    #gray = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    x1 = cv2.resize(x, (300, 300))
    p_tb = tb_model.predict(numpy.expand_dims(x1,axis=0))
    #print(p_tb)
    return p_tb


#labels = ["NORMAL", "PNEUMONIA"]
def pnm_predict(image):
    #img_array = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(image, (50, 50))
    new_array = new_array.reshape(-1, 50, 50, 1)
    prediction = pnm_model.predict(new_array)
    return prediction






