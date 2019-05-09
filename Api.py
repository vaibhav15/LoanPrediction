#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:06:43 2019

@author: miracle
"""


import flask
from cust import customer
from flask import jsonify

from flask import Flask,request
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return (jsonify("Hello"))


@app.route('/model',methods=['GET','POST'])
def model():
    #SSN =request.form['ssn']
    #Tenure = request.form['tenure']
    #loan_amount = request.form['loan_amount'] 
    #loan_type = request.form['loan_type']
    loan_amnt = request.form['loan_amnt']
    emp_length = request.form['emp_length']
    home_ownership = request.form['home_ownership']
    annual_inc = request.form['annual_inc']
    dti = request.form['dti']
    purpose = request.form['purpose']
    fico_average = request.form['fico_average']
    tenure = request.form['tenure']
    
    instance_c = customer(loan_amnt, emp_length, home_ownership, annual_inc, dti, purpose, fico_average,tenure)
    
    result = instance_c.final_output()
    print(result)
    return(jsonify(result))
    #return(result)
    
if __name__=="__main__":
    app.run()