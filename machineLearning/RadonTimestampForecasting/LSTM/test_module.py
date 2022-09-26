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
    
    
def multi(a,b):
    print(a*b)
    
def printer():
    print("Hahhahaahah")
    
def anotherOne():
    print("warels")
