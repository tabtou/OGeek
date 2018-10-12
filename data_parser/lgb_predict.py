# coding=utf-8

# coding=utf-8

import lightgbm as lgb
import pandas as pd
import numpy as np

data=pd.read_csv('./data/data.csv')


train1 =data[data.flag==0]
train2 = data[data.flag==1]



train = pd.concat([train2,train1])
del train1, train2
train_y = train.label
# test_y = test.label
train_x = train.drop(['label','flag'], axis=1)
# test_x = test.drop(['label','flag'], axis=1)

del train
lgb_train = lgb.Dataset(train_x, train_y)
del train_x, train_y



test  = data[data.flag==2]

test = test.drop(['label','flag'], axis=1)


params = {
    'boosting_type': 'gbdt',
    'objective': 'binary',
    'metric': 'None',
    'num_leaves': 30,
    'learning_rate': 0.1,
    'feature_fraction': 0.75,
    'bagging_fraction': 0.75,
    'lambda_l1': 2.0,
    'lambda_l2': 5.0,
    'min_gain_to_split': 0.01,
    'min_sum_hessian_in_leaf': 1.0,
    'max_depth': 5,
    'bagging_freq': 1
}

def f1_error(preds,y_label):
    label=y_label.get_label()

    preds = [int(i >= 0.4) for i in preds]
    tp=sum([int(i==1 and j==1)for i,j in zip(preds,label)])
    precision=float(tp)/sum(preds)
    recall=float(tp)/sum(label)
    return 'f1-score',2*(precision*recall/(precision+recall)),True






gbm = lgb.train(params,
                lgb_train,
                feval = f1_error,
                num_boost_round=2000,
                categorical_feature=['tag'])


# print(str(gbm.best_score))
# pred_test = gbm.predict(test_x)
# submit_test=pd.DataFrame(pred_test)
# submit_test.columns=['predict_socre']
# submit_test.predict_socre=submit_test.predict_socre.apply(lambda x:1 if x>=0.4 else 0)
# f1score = f1_error(submit_test,test_y)
# print(str(f1score))

pred = gbm.predict(test)
submit=pd.DataFrame(pred)

submit.columns=['predict_socre']
print(submit.info())
submit.predict_socre=submit.predict_socre.apply(lambda x:1 if x>=0.4 else 0)
print(submit.describe())
submit.to_csv("lgb_10_10.csv", index=None,header=None)
