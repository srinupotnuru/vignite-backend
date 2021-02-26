import pandas as pd 
import numpy as np
from flask import Flask, request
from flask_cors import CORS , cross_origin
import os
ds=pd.read_csv('dataset.csv')
l1=ds.Crop  
l2=ds.Crop_Year 
l3=ds.Production
l4=set(l1)
def get_crop_year(st):
    lis=[]
    for i in range(len(l1)):
        if l1[i]==st:
            lis.append({'y':l3[i],'label':l2[i]})
    return lis 

def get_area_prod():
    ans=[]
    for i in range(len(l2)):
        ans.append({'y':l2[i],'x':l3[i]})
    return ans 
def year_wise_crops():
    ans=[]
    for val in l4:
        temp=get_crop_year(val)
        ans.append({val:temp})
    return ans 


app=Flask(__name__)
cors=CORS(app)
app.config['CROS_HEADERS']='Content-type'
Port=int(os.getenv('PORT',8000))

if __name__ =='__main__':
    app.run(host='0.0.0.0',port=port,debug=True)