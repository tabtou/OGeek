import xgboost as xgb

import pandas as pd
import numpy as np

data=pd.read_csv('./data/data.csv')


train1 =data[data.flag==0]
train2 = data[data.flag==1]



train = pd.concat([train2,train1])
del train1, train2
train_y = train.label
train_x = train.drop(['label','flag'], axis=1)