import tensorflow as tf
from tensorflow.keras.regularizers import l2
import os
import numpy as np

vocab_size=10000

def build():

    encoder = tf.keras.layers.experimental.preprocessing.TextVectorization(max_tokens=vocab_size)
    
    model = tf.keras.Sequential( [
    encoder,
    tf.keras.layers.Embedding(input_dim=vocab_size+1,output_dim=64,mask_zero=True),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64,  return_sequences=True,kernel_regularizer=l2(0.01))),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32,kernel_regularizer=l2(0.01))),

    tf.keras.layers.Dense(64, activation='relu',kernel_regularizer=l2(0.01)),
    tf.keras.layers.Dropout(0.5),
    
    tf.keras.layers.Dense(32, activation='relu',kernel_regularizer=l2(0.01)),
    tf.keras.layers.Dropout(0.5),

    tf.keras.layers.Dense(16, activation='relu',kernel_regularizer=l2(0.01)),
    tf.keras.layers.Dropout(0.5),
    
    tf.keras.layers.Dense(1,activation='sigmoid')
    ])

    return model

