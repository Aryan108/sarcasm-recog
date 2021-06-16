import streamlit as st
import numpy as np
from builder import build

model = build()
print("Built model")
model.load_weights('weights/mod1')


def main():
    st.title("Sarcastic News Prediction")
    input=st.text_input("Enter the text")
    if len(input) > 0:
        st.write('',predict_output(input))
    return
    
def predict_output(input):
    input = np.array([input])
    pred = model.predict(input)
    out = pred[0][0]*100
    if out >= 50:
        return f"Sarcasm with {out:.2f}% confidence"
        #st.markdown('<h4 style="color:#4caf50"> Sarcasm </h4>',unsafe_allow_html=True)
    else :
        return f"Not Sarcasm with {(100-out):.2f}% confidence"
        #st.markdown('<h4 style="color:#455a64"> Not Sarcasm </h4>',unsafe_allow_html=True)
        #st.write(':neutral_face: ')



if __name__=='__main__':
    main()