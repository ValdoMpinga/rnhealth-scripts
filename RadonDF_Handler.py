#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from datetime import timezone, datetime
import os
    
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
def df_to_X_y(df,hoursToPredict, window_size):
        hoursToPredict = hoursToPredict - 1
        df_as_np = df.to_numpy() # converts the dataframe to a numpy array
        #Initialized  arrays to append X and Y values 
        X = []
        y = []
        for i in range(len(df_as_np)):
            if((i + hoursToPredict + window_size)< len(df_as_np)):
                #Takes values from i to i + win size
                row =  [r for r in df_as_np[i:i+window_size]]
                X.append(row)
                label = df_as_np[i + hoursToPredict + window_size ][0]
                y.append(label)
        return np.array(X), np.array(y)

#Returns the data organized according to how many hours we want to forecast
def Handler(hoursToPredict,window_size):
    imputedMeasurementsDf = pd.read_csv('./../../../Data/ProcessedData/Interpolation/interpolatedMeasurementsDf.csv')
    imputedMeasurementsDf = pd.DataFrame(imputedMeasurementsDf)
    print(imputedMeasurementsDf['time'][0])
    imputedMeasurementsDf['time'] =  pd.to_datetime(imputedMeasurementsDf['time'], format='%Y-%m-%d %H:%M:%S')
    print(imputedMeasurementsDf.head())
    measurementsTime['time'] = pd.DataFrame(imputedMeasurementsDf['time']).astype({'time':''})
    print(type(imputedMeasurementsDf['time'][0]))

    dateTimeDf = pd.DataFrame(measurementsDf['time'])

    measurementsDf = dateTimeDf.join(imputedMeasurementsDf.drop(['day','month','hour'],axis = 1))
    measurementsDf.index =measurementsDf['time']

    iso8601ToDatetime(dateTimeDf)

    df =pd.DataFrame( measurementsDf['Rn'])

    df['H'] = measurementsDf['H']
    df['CO2'] = measurementsDf['CO2']
    df['P'] = measurementsDf['P']
    df['T'] = measurementsDf['T']

    X1, y1 = df_to_X_y(df,hoursToPredict,window_size)
    return X1, y1


