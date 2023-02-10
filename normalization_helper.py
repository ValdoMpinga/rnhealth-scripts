import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd

def datasetScaler(df):
    scaler = StandardScaler()
    scaler.fit(df)

    normalized_df = pd.DataFrame(scaler.transform(
        df), columns=df.columns, index=df.index)

    return normalized_df, scaler

def inverse_scale_1d(array, scaler, column, data):
    col_scaler = StandardScaler().fit(data[[column]])
    inverse_scaled_value = col_scaler.inverse_transform(array.reshape(-1, 1))
    return inverse_scaled_value


def normalize_forecast_input_data(data, means, stds):
    """
    Normalize a single input to prepare it for prediction.

    Parameters:
    - data: a list of lists, where each list inside represents a row of data
    - means: a list of means for each column
    - stds: a list of standard deviations for each column

    Returns:
    - normalized_data: a list of lists, where each list inside represents a row of normalized data
    """
    normalized_data = []
    for i in range(len(data)):
        normalized_row = [(data[i][j] - means[j]) / stds[j]
                        for j in range(len(data[i]))]
        normalized_data.append(normalized_row)
    return [normalized_data]


def inverse_normalize_value(normalized_value, mean, std):
    original_value = normalized_value * std + mean
    return original_value


def inverse_forecast_normalize_data(normalized_data, means, stds):
    """
    Inverse normalize a single input to realize the prediction.

    Parameters:
    - data: a list of lists, where each list inside represents a row of data
    - means: a list of means for each column
    - stds: a list of standard deviations for each column

    Returns:
    - inverse_normalized_data: a list of lists, where each list inside represents a row of inverse normalized data
    """
    original_data = []
    for i in range(len(normalized_data)):
        if len(normalized_data[i]) != len(means) or len(normalized_data[i]) != len(stds):
            raise ValueError(
                "Length of normalized data row and means or stds must be equal.")
        original_row = [normalized_data[i][j] * stds[j] + means[j]
                        for j in range(len(normalized_data[i]))]
        original_data.append(original_row)
    return original_data


def df_to_X_y(df, hoursToPredict, windowSize):
    hoursToPredict = hoursToPredict - 1
    df_as_np = df.to_numpy()  # converts the dataframe to a numpy array
    # Initialized  arrays to append X and Y values
    X = []
    y = []
    for i in range(len(df_as_np)):
        if ((i + hoursToPredict + windowSize) < len(df_as_np)):
            # Takes values from i to i + win size
            row = [r for r in df_as_np[i:i+windowSize]]
            X.append(row)
            label = df_as_np[i + hoursToPredict + windowSize][1]
            y.append(label)
    return np.array(X), np.array(y)

def mae(y_true, predictions):
    y_true, predictions = np.array(y_true), np.array(predictions)
    return np.mean(np.abs(y_true - predictions))

def datasetCleaner(df):
    df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S')
    df.index = df['time']
    df = df.drop(['time'], axis=1)
