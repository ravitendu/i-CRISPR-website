#----------import dependencies-----------
import numpy as np
from keras.models import load_model
import pandas as pd

#----------Load model-----------
model = load_model("utils/Deep_learning_Backend_codes/Fnn_model_accepted.h5")

#----------Load user data-----------
def run2():

    user_data=pd.read_csv("utils/Encoded_input_data.csv",header=None)
    row=int(len(user_data)/10)

    #----------Convert user data into array-----------
    array=np.array(user_data)
    newarray_x=[]
    newarray_y=[]
    start=0
    for ii in range(row):
        takedata=array[start:start+10,:]
        newarray_x.append(takedata)
        newarray_y.append(array[start,])
        start+=10
    datax=newarray_x
    y_test=np.array(newarray_y)
    # print("This is y_test\n",y_test)
    data = []
    for ii in datax:
        df = np.reshape(ii, (10*23))
        data.append(df)
    # x_test=np.array(data)
    x_test=np.array(data,dtype='int16')
    # print("This is x_test\n",x_test)

    #----------Predict output-----------
    y_predc = model.predict(x_test)
    y_pred=y_predc >=0.5
    y_pred=y_pred.argmax(axis=1)
    # print(y_pred)

    # -------Code For generating Excel file for user------
    Result_output=pd.read_excel("utils/input_data.xlsx")
    Result_output.set_index('sgRNA', inplace=True)
    Result_output["Result"]=y_pred
    # print(Result_output)
    Result_output.to_excel("utils/i-CRISPR(DL)_result.xlsx")
    Result_output.to_csv("utils/i-CRISPR(DL)_result.csv")