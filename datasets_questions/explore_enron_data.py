#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
from pandas import ExcelWriter
import pickle
import pandas as pd
import xlsxwriter
enron_data = pickle.load(open(r"C:\Users\Tanmay\Documents\GitHub\ud120-projects\final_project\final_project_dataset.pkl", "r"))
df=pd.DataFrame(enron_data)
df=df.T
writer= ExcelWriter('PythonExport1.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='sheet 1')
writer.save()
results = []

'''with open(r'C:\Users\Tanmay\Documents\GitHub\ud120-projects\final_project\poi_names.txt') as inputfile:
    for line in inputfile:
        results.append(line.strip().split(','))
'''
