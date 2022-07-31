import numpy as np
import pandas as pd
import math

order_data = pd.DataFrame(pd.read_excel('附件1 近5年402家供应商的相关数据.xlsx',sheet_name=0))
offer_data = pd.DataFrame(pd.read_excel('附件1 近5年402家供应商的相关数据.xlsx',sheet_name=0))

order_data_a = order_data.loc[offer_data['材料分类'] == 'A'].reset_index(drop=True) 
order_data_b = order_data.loc[offer_data['材料分类'] == 'B'].reset_index(drop=True) 
order_data_c = order_data.loc[offer_data['材料分类'] == 'C'].reset_index(drop=True) 

offer_data_a = offer_data.loc[offer_data['材料分类'] == 'A'].reset_index(drop=True) 
offer_data_b = offer_data.loc[offer_data['材料分类'] == 'B'].reset_index(drop=True) 
offer_data_c = offer_data.loc[offer_data['材料分类'] == 'C'].reset_index(drop=True) 

order_data_a.to_excel('订货A.xlsx')
order_data_b.to_excel('订货B.xlsx')
order_data_c.to_excel('订货C.xlsx')

offer_data_a.to_excel('供货A.xlsx')


print(order_data.describe())
print(offer_data.describe())
