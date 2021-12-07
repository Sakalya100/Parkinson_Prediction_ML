# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle 


loaded_model = pickle.load(open('D:/My Learning/ML Projects/ML Challenge/SVM_Prediction_Model_Parkinson.sav','rb'))

input_data = [119.992,157.302,74.997,0.00784,7e-05,0.0037,0.00554,0.011090000000000001,0.04374,0.426,0.02182,0.0313,
              0.029710000000000004,0.06545,0.022109999999999998,21.033,0.414783,0.815285,-4.813031,0.266482,2.3014419999999998,
              0.284654]

input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]==0):
    print("The person doesn't have Parkinson's Disease")
else:
    print("The person have Parkinson's Disease")

