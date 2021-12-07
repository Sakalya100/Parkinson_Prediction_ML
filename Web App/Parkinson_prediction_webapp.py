# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 23:17:35 2021

@author: SAKALYA
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('D:/My Learning/ML Projects/ML Challenge/SVM_Prediction_Model_Parkinson.sav','rb'))

# creating a function for prediction

def parkinson_predict(input_data):
    

    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if (prediction[0]==0):
        return "The person doesn't have Parkinson's Disease"
    else:
        return "The person have Parkinson's Disease"




def main():
    
    # giving title to the webpage
    
    st.title('Parkinson Prediction Web App')
    
    # getting the input data from the user
    
    
    MDVP_Fo = st.text_input("Average vocal fundamental frequency")
    MDVP_Fhi = st.text_input("Maximum vocal fundamental frequency")
    MDVP_Flo = st.text_input("Minimum vocal fundamental frequency")
    MDVP_JitP = st.text_input("Measure of frequency 1")
    MDVP_JitA = st.text_input("Measure of frequency 2")
    MDVP_RAP = st.text_input("Measure of frequency 3")
    MDVP_PPQ = st.text_input("Measure of frequency 4")
    Jit_DDP = st.text_input("Measure of frequency 5")
    MDVP_Shim = st.text_input("Measure of Amplitude 1")
    MDVP_ShimD = st.text_input("Measure of Amplitude 2")
    Shim_APQ3 = st.text_input('Measure of Amplitude 3')
    Shim_APQ5 = st.text_input("Measure of Amplitude 4")
    MDVP_APQ = st.text_input("Measure of Amplitude 5")
    Shim_DDA = st.text_input('Measure of Amplitude 6')
    NHR = st.text_input("Ratio of Noise of tonal components 1")
    HNR = st.text_input("Ratio of Noise of tonal components 2")
    RPDE = st.text_input("Nonlinear dynamical complexity measures 1")
    DFA = st.text_input("Signal fractal scaling exponent")
    spread1 = st.text_input("Nonlinear measures of fundamental frequency variation 1")
    spread2 = st.text_input("Nonlinear measures of fundamental frequency variation 2")
    D2 = st.text_input("Nonlinear dynamical complexity measures 2")
    PPE = st.text_input("Nonlinear measures of fundamental frequency variation 3")
    
    
    # code for prediction
    
    diagnosis = ''
    
    # About creating a button for prediction
    
    if st.button('Parkinson Test Result'):
        diagnosis = parkinson_predict([MDVP_Fo,MDVP_Fhi,MDVP_Flo,
                                       MDVP_JitP,MDVP_JitA,MDVP_RAP,
                                       MDVP_PPQ,Jit_DDP,MDVP_Shim,
                                       MDVP_ShimD,Shim_APQ3,Shim_APQ5,
                                       MDVP_APQ,Shim_DDA,NHR,HNR,
                                       RPDE,DFA,spread1,spread2,
                                       D2,PPE])
        
        st.success(diagnosis)
        
        
        
if __name__ == '__main__':
    main()