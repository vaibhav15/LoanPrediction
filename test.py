#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 15:36:52 2019

@author: miracle
"""
loan_amnt = 5000
emp_length = "2 years"
home_ownership = "RENT"
annual_inc = 4000
dti = 12.0
purpose = "educational"
fico_average = 700
tenure = 36
categorical_input = {}
        
        
categorical_input["emp_length"] = emp_length
categorical_input["home_ownership"] = home_ownership
categorical_input["purpose"] = purpose


import pandas as pd

col = ['loan_amnt', 'annual_inc', 'dti', 'fico_average', 'tenure', 'OTHER',
 'OWN', 'RENT', 'credit_card', 'debt_consolidation', 'educational', 'home_improvement',
 'house', 'major_purchase', 'medical', 'moving', 'other', 'renewable_energy', 'small_business',
 'vacation', 'wedding', 'more than 10 years', '2 years', '3 years', '4 years', '5 years',
 '6 years', '7 years', '8 years', '9 years', 'less than 1 year']


df = pd.DataFrame(columns = col,index=[0])

df.loc[0,'loan_amnt'] = loan_amnt
df.loc[0,'annual_inc'] = annual_inc
df.loc[0,'dti'] = dti
df.loc[0,'fico_average'] = fico_average
df.loc[0,"tenure"] = tenure

dict_categorical = {'home_ownership': ['OTHER', 'OWN', 'RENT'],
 'purpose': ['credit_card',  'debt_consolidation',  'educational',
  'home_improvement',  'house',  'major_purchase',  'medical',  'moving', 
  'other',  'renewable_energy',  'small_business',  'vacation',  'wedding'],
 'emp_length': [ 'more than 10 years',  '2 years',  '3 years',
  '4 years',  '5 years',  '6 years',  '7 years',
  '8 years',  '9 years',  'less than 1 year']}
        
for key,element in dict_categorical.items():
    for key1,element1 in categorical_input.items():
        if key == key1:
            for i in element:
                if i == element1 :
                    df.loc[0,i] = int(1)
                else:
                    df.loc[0,i] = (0)
                
df.dtypes                
                
df.loc[:,col].values                
                
                
                
                