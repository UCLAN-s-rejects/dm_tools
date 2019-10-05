import os
from dotenv import load_dotenv
from flask import Flask, request
import random
import dotenv
from data_load import load_data_arrays

#find .env file
dotenv_path=dotenv.find_dotenv()
load_dotenv(dotenv_path)

# load env variables

low_val=os.getenv('low_val_csv')
med_val=os.getenv('med_val_csv')
high_val=os.getenv('high_val_csv')
vhigh_val=os.getenv('vhigh_val_csv')

app = Flask(__name__)

@app.route('/test', methods = ['POST'])
def randomiser():
    if "weightings" in request.json:
        l=request.json["weightings"][0]
        m=request.json["weightings"][1]
        h=request.json["weightings"][2]
        vh=request.json["weightings"][3]
        data=load_data_arrays(low_val,med_val,high_val,vhigh_val)
        total=(l+m+h+vh)
        tier=random.randint(1,total+1)

        if tier>=1 and tier<=l:
            response={}
            length=len(data["low"]["Name"])
            selection=random.randint(1,length+1)
            response["item"]=data["low"]["Name"][selection]
            response["url"]=data["low"]["URL"][selection]

        elif tier>l and tier<=l+m:
            response={}
            length=len(data["medium"]["Name"])
            selection=random.randint(1,length+1)
            response["item"]=data["medium"]["Name"][selection]
            response["url"]=data["medium"]["URL"][selection]

        elif tier>l+m and tier<=l+m+h:
            response={}
            length=len(data["high"]["Name"])
            selection=random.randint(1,length+1)
            response["item"]=data["high"]["Name"][selection]
            response["url"]=data["high"]["URL"][selection]

        elif tier>l+m+h and tier<=total:
            response={}
            length=len(data["vhigh"]["Name"])
            selection=random.randint(1,length+1)
            response["item"]=data["vhigh"]["Name"][selection]
            response["url"]=data["vhigh"]["URL"][selection]

        return response
    else:
        return "include wieghtings"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=3000)
