import random
from evaluator import *
import numpy as np
import pandas as pd
from poker import *

name ='P3'
conf = pd.read_csv("mlfiles\\confidenceValues.csv", usecols=['P1', 'P2', 'P3', 'P4', 'P5'])
conf.at[0,
        name] = conf.at[0, name]+1
print(conf)