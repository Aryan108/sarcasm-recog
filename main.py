import json
import nltk
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
import numpy as np

def predict(user_input):
    model = tf.keras.models.load_model('./saved_model/1',compile=False)
    
    acc = model.predict(np.array([user_input]))
    acc = acc[0][0]
    
    if acc > 0.5:
        text = "Sarcasm with {}% accuracy".format(round(acc*100))
        color = [0,255,0]
    elif acc < 0.5:
        text = "Not Sarcasm with {}% accuracy".format( round((1 - acc)*100) )
        color = [255,0,0]
    else:
        text = "Sarcasm with 50% accuracy"
        color = [255,255,255]
    return text,color
