#Indoor Radon Concentration Forecasting

This GitHub repository contains Jupyter notebooks with Python code for implementing and evaluating two LSTM-based approaches for indoor radon concentration forecasting. 
The goal of this project is to leverage Machine Learning (ML) techniques to predict future levels of indoor radon gas based on past and current data. 
Accurate forecasting of indoor radon levels enables effective management of indoor radon risk and helps mitigate human exposure.

#Abstract

Indoor radon is a radioactive gas that can accumulate in homes, posing a health risk to humans. 
Forecasting indoor radon levels is crucial for mitigating exposure risk and effectively managing indoor radon. 
Machine Learning (ML) techniques, such as LSTM-based approaches, enable the prediction of future indoor radon levels based on historical and current data. 
This work presents preliminary results of implementing and evaluating two LSTM-based approaches for indoor radon forecasting.
The forecasts obtained from these models serve as a tool to trigger preventive management procedures for Indoor Air Quality management.
Preliminary results indicate that the Long Short-Term Memory (LSTM) algorithm, applied to normalized data, proves to be the optimal approach for this application.
The LSTM-based approach demonstrates superior accuracy across various forecasting time windows compared to other approaches evaluated in this work.

#Repository Structure

normalization_helper.py: Contains code for data normalization and denormalization, making it easier to preprocess the data.

trainer_helper.py: Provides helper functions for the training process, aiding in the model development and optimization.

LSTM/: Contains LSTM model implementations.

D001/: Represents a specific sensor and contains the corresponding LSTM models trained on it.

<Hour>_Forecast/: This folder structure represents the forecast duration, ranging from 1 to 6 hours. Inside each folder, you can find the LSTM models that forecast the indoor radon concentration for the specified duration.
D003/: Represents another specific sensor and follows the same structure as D001/.

bi-LSTM/: Contains Bidirectional LSTM model implementations.

D001/: Represents a specific sensor and contains the corresponding Bidirectional LSTM models trained on it.

<Hour>_Forecast/: This folder structure represents the forecast duration, ranging from 1 to 6 hours. Inside each folder, you can find the Bidirectional LSTM models that forecast the indoor radon concentration for the specified duration.

D003/: Represents another specific sensor and follows the same structure as D001/.

README.md: The current file, providing an overview of the repository and its contents.

This work is a result of the project TECH - Technology, Environment, Creativity and Health, Norte-01-0145-FEDER-000043, supported by Norte Portugal Regional Operational Program (NORTE 2020), under the PORTUGAL 2020 Partnership Agreement, through the European Regional Development Fund (ERDF)
