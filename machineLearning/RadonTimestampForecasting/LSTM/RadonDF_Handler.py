#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[2]:

import tensorflow as tf
import os
import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
from datetime import timezone, datetime
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler 
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.metrics import RootMeanSquaredError,MeanAbsoluteError
from tensorflow.keras.metrics import Accuracy
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model

os.environ['KMP_DUPLICATE_LIB_OK']='True'
import absl.logging
absl.logging.set_verbosity(absl.logging.ERROR)
    
#Converts the datetime string in iso 8601 format to python datetime format
def iso8601ToDatetime(dateTimeDf):
    for i in range(len(dateTimeDf['time'])):
        timeContainer  = dateTimeDf['time'][i].replace('.000','')
        timeContainer = datetime.strptime(timeContainer, "%Y-%m-%dT%H:%M:%SZ")
        timeContainer = int(round(timeContainer.timestamp()))
        timeContainer = datetime.fromtimestamp(timeContainer)
        dateTimeDf['time'][i] = timeContainer

#Converts the Df to a numpy array and then extracts the X and y value
#on the required format to train the model

def df_to_X_y(df, window_size=6):
    df_as_np = df.to_numpy() # converts the dataframe to a numpy array
    #Initialized  arrays to append X and Y values 
    X = []
    y = []
    for i in range(len(df_as_np)):
        if((i + 4 + window_size)< len(df_as_np)):
            #Takes values from i to i + win size
            row =  [r for r in df_as_np[i:i+window_size]]
            X.append(row)
            #The final output
            #print(( i + window_size))
            label = df_as_np[i + 4 + window_size ][0]
            y.append(label)
    return np.array(X), np.array(y)

def Handler(hoursToPredict):
    imputedMeasurementsDf = pd.read_csv('../../../../../../Data/ProcessedData/KnnImputed/measurementsImputedByKnn.csv')
    measurementsDf = pd.read_csv('../../../../../../Data/RawData/rawMeasurementsFilteredBySensors.csv')

    dateTimeDf = pd.DataFrame(measurementsDf['time'])

    measurementsDf = dateTimeDf.join(imputedMeasurementsDf.drop(['day','month','hour'],axis = 1))
    measurementsDf.index =measurementsDf['time']

    iso8601ToDatetime(dateTimeDf)

    df =pd.DataFrame( measurementsDf['Rn'])

    df['H'] = measurementsDf['H']
    df['CO2'] = measurementsDf['CO2']
    df['P'] = measurementsDf['P']
    df['T'] = measurementsDf['T']

    X1, y1 = df_to_X_y(df)
    return X1, y1



def Printer():
    print("Snowfall")
# In[3]:





# In[ ]:




