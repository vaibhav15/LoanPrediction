#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:54:50 2019

@author: miracle
"""

from cust import customer
from flask import jsonify

#a= customer()
#test = a.final_output('123456789','12','20000','car')
#print (test)
a= customer(
    loan_amnt = 500,
    emp_length = "8 years",
    home_ownership = "RENT",
    annual_inc = 50000,
    dti = 1.0,
    purpose = "educational",
    fico_average = 700,
    tenure = 36
    )
test = a.final_output()

print(test)


if __name__== "__main__":
    a= customer(
        loan_amnt = 500,
        emp_length = "8 years",
        home_ownership = "RENT",
        annual_inc = 50000,
        dti = 1.0,
        purpose = "educational",
        fico_average = 700,
        tenure = 36
        )
    test = a.final_output()

    print ("result is")
    print(test)
    #print (jsonify(customers=test))    