# Import required libraries
import pickle
import pandas as pd
# Load the RFC model as .sav file

def run2():
    with open('utils/Machine_learning_Backend_codes/Rfc_model_accepted.sav', 'rb') as f:
        rfc_model = pickle.load(f)
    # Make predictions using the loaded model
    X = pd.read_csv("utils/input_features.csv")
    Y = rfc_model.predict(X)
    # Print the predicted outputs
    print(Y)
    # print(len(Y))
    # -------Code For generating Excel file for user------
    Result_output=pd.read_csv("utils/input_data.csv")
    Result_output.set_index('sgRNA', inplace=True)
    Result_output["Result"]=Y
    # print(Result_output)
    Result_output.to_csv("utils/i-CRISPR(ML)_result.csv")