import pandas as pd
import dotenv
from dotenv import load_dotenv
import os

#find .env file
dotenv_path=dotenv.find_dotenv()
load_dotenv(dotenv_path)

# load env variables

low_val=os.getenv('low_val_csv')
med_val=os.getenv('med_val_csv')
high_val=os.getenv('high_val_csv')
vhigh_val=os.getenv('vhigh_val_csv')

def load_data_arrays(low,medium,high,vhigh):
    data={}
    data["low"]=pd.read_csv(low,encoding="utf-8")
    data["medium"]=pd.read_csv(medium,encoding="utf-8")
    data["high"]=pd.read_csv(high,encoding="utf-8")
    data["vhigh"]=pd.read_csv(vhigh,encoding="utf-8")
    return data


