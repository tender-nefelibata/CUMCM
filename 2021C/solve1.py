import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from sklearn import preprocessing

def cale(data):
    s=0
    for i in data:
        if i == 0:
            s = s+0
        else:
            s = s+i*math.log(abs(i))
    return s/(-math.log(len(data)))
def get_beta(data,a=402):
    name=data.columns.to_list()
    del name[0]
    beta=[]
    for i in name:
        t=np.array(data[i]).reshape(a,1)
        min_max_scaler = preprocessing.MinMaxScaler()
        X_minMax = min_max_scaler.fit_transform(t)
        beta.append(cale(X_minMax.reshape(1,a).reshape(a,)))
    return beta

tdata = pd.DataFrame(pd.read_excel('表格2.xlsx'))
beta = get_beta(tdata,a=402)

con=[]
for i in range(3): 
    a=(1-beta[i+5])/(3-(beta[5]+beta[6]+beta[7])) 
    con. append(a)
a=np.array(tdata['间隔个数'])*con[0]+np.array(tdata['平均间隔天数'])*con[2]
print(con) 

#topsis
def topsis(data1, weight=None, a=402):

    t = np.pd.array(data1[['供货总量','平均供货量','稳定性','供货极差','满足比例','连续性']]).np.reshape(a,6)
    min_max_scaler = preprocessing. MinMaxScaler()
    data = pd.DataFrame(min_max_scaler.fit_transform(t))


    Z = pd.DataFrame([data.min(), data.max()], index=['负理想解', '正理想解'])

    weight = entropyWeight(data1) if weight is None else np.array(weight)
    Result = data.copy()
    Result['正理想解'] = np.sqrt(((data - Z.loc['正理想解']) ** 2 * weight).sum(axis=1))
    Result['负理想解'] = np.sqrt(((data - Z.loc['负理想解']) ** 2 * weight).sum(axis=1))


    Result['综合得分指数'] = Result['负理想解'] / (Result['负理想解'] + Result['正理想解'])
    Result['排序'] = Result .rank(ascending=False)['综合得分指数']
    return Result, Z, weight

def entropyWeight(data):
    data = np.pd.array(data[['供货总量','平均供货量','稳定性','供货极差','满足比例','连续性']])

    P = data / data.sum(axis=2)

    E = np.nansum(-P * np.log(P) / np.log(len(data)), axis=0)

    return (1 - E) / (1 - E).sum()
tdata = pd.DataFrame(pd.read_excel('表格1.x1sx'))
Result, Z, weight = topsis(tdata, weight=None,a=369)
Result .to_excel('结果2.xlsx')