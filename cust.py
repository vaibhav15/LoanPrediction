# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""




class customer:
    def __init__(self,loan_amnt, emp_length, home_ownership, annual_inc, dti, purpose, fico_average,tenure ):

        #self.loan_amnt = 5000
        #self.emp_length = "2 years"
        #self.home_ownership = "RENT"
        #self.annual_inc = 4000
        #self.dti = 12.0
        #self.purpose = "educational"
        #self.fico_average = 700
        #self.tenure = 36
        
        
#       
        self.loan_amnt = float(loan_amnt)
        self.emp_length = emp_length
        self.home_ownership = home_ownership
        self.annual_inc = float(annual_inc)
        self.dti = float(dti)
        self.purpose = purpose
        self.fico_average = float(fico_average)
        self.tenure = float(tenure)
        self.categorical_input = {}
        
        
        self.categorical_input["emp_length"] = emp_length
        self.categorical_input["home_ownership"] = home_ownership
        self.categorical_input["purpose"] = purpose
        
        
        import pandas as pd
        
        self.col = ['loan_amnt', 'annual_inc', 'dti', 'fico_average', 'tenure', 'OTHER',
         'OWN', 'RENT', 'credit_card', 'debt_consolidation', 'educational', 'home_improvement',
         'house', 'major_purchase', 'medical', 'moving', 'other', 'renewable_energy', 'small_business',
         'vacation', 'wedding', 'more than 10 years', '2 years', '3 years', '4 years', '5 years',
         '6 years', '7 years', '8 years', '9 years', 'less than 1 year']
        
        
        self.df = pd.DataFrame(columns = self.col,index=[0])
        
        self.df.loc[0,'loan_amnt'] = self.loan_amnt
        self.df.loc[0,'annual_inc'] = self.annual_inc
        self.df.loc[0,'dti'] = self.dti
        self.df.loc[0,'fico_average'] = self.fico_average
        self.df.loc[0,"tenure"] = self.tenure
        
        self.dict_categorical = {'home_ownership': ['OTHER', 'OWN', 'RENT'],
         'purpose': ['credit_card',  'debt_consolidation',  'educational',
          'home_improvement',  'house',  'major_purchase',  'medical',  'moving', 
          'other',  'renewable_energy',  'small_business',  'vacation',  'wedding'],
         'emp_length': [ 'more than 10 years',  '2 years',  '3 years',
          '4 years',  '5 years',  '6 years',  '7 years',
          '8 years',  '9 years',  'less than 1 year']}
#####
##### Categorical_input is taken from the argument                
        for self.key,self.element in self.dict_categorical.items():
            for self.key1,self.element1 in self.categorical_input.items():
                if self.key == self.key1:
                    for self.i in self.element:
                        if self.i == self.element1 :
                            self.df.loc[0,self.i] = 1
                        else:
                            self.df.loc[0,self.i] = 0
                        
                
        

    

        
    def final_output(self):
        import pickle 
        import numpy as np
        
        self.risk_category = "New"
        self.interest = 0.0
        self.Loan_Amount_Approved = 0
        self.Tenure_Approved = 0 
        self.emi = 0
        
        self.X = self.df.loc[:,self.col].values
        
        
        self.filename = 'xgb_model_final.sav'
        self.loaded_model = pickle.load(open(self.filename, 'rb'))
       
        self.predictions = self.loaded_model.predict_proba(self.X)
        
        if self.predictions[0][1] >= 0.5:
            self.risk_category = "Rejected"
            self.interest = round(float(np.random.normal(9, 1, 1)[0]),2)
            self.Tenure_Approved = 0
            self.df["risk_category"] = 2
        elif self.predictions[0][1] >= 0.2:
            self.risk_category = "Medium Risk"
            self.interest = round(float(np.random.normal(6, 1, 1)[0]),2)
            self.Tenure_Approved = self.tenure
            self.df["risk_category"] = 1
        else:
            self.risk_category = "Low Risk"
            self.interest = round(float(np.random.normal(3, 1, 1)[0]),2)
            self.Tenure_Approved = self.tenure
            self.df["risk_category"] = 0
        
        
       # self.file_name1 = "/home/miracle/Desktop/Python API of Informatica/Testing/test_data_coversion.csv"
       # self.df.to_csv(self.file_name1,index=False)
        
        self.Loan_Amount_Approved = float(round(self.loan_amount_cal(),0))
        
        if self.Loan_Amount_Approved < 0:
            self.Loan_Amount_Approved = 0
        
        if self.risk_category == "Low Risk":
            self.Loan_Amount_Approved = self.loan_amnt
        
        self.emi = float(self.emi_calculator(self.Loan_Amount_Approved,self.interest,
                                       self.Tenure_Approved))
        
        self.out = list()
        self.out.append(self.risk_category)
        self.out.append(self.interest)
        self.out.append(self.Loan_Amount_Approved)
        self.out.append(self.Tenure_Approved)
        self.out.append(self.emi)
        self.list1 = ['Prediction','Interest','Amount_Approved','Tenure','EMI']
        self.final_out = dict(zip(self.list1, self.out))
        return (self.final_out)
        

    def loan_amount_cal (self):
        import pickle 
        import numpy as np
        self.X_loan_amount = self.df[['risk_category','annual_inc', 'dti', 'fico_average', 'tenure', 'OTHER',
         'OWN', 'RENT', 'credit_card', 'debt_consolidation', 'educational', 'home_improvement',
         'house', 'major_purchase', 'medical', 'moving', 'other', 'renewable_energy', 'small_business',
         'vacation', 'wedding', 'more than 10 years', '2 years', '3 years', '4 years', '5 years',
         '6 years', '7 years', '8 years', '9 years', 'less than 1 year']]

        self.filename1 = 'xgb_regressor_amount.sav'
        self.loaded_model = pickle.load(open(self.filename1, 'rb'))
       
        self.preds = self.loaded_model.predict(self.X_loan_amount.values)                            
                  
        return (round(self.preds[0],2))
        
    
    def emi_calculator(self,p, r, t): 
        self.r = r / (12 * 100) # one month interest 
        self.t = t # one month period 
        self.p = p
        self.emi_cal = (self.p * self.r * pow(1 + self.r, self.t)) / (pow(1 + self.r, self.t) - 1) 
        return (round(self.emi_cal,2)) 

    
#if __name__== "__main__":
#    a= customer('Vaibhav',25)
#    test = a.print_output()
#    print(test)
