# Programme for taking user input and writing it in Excel file
import tkinter as tk
from tkinter import filedialog
import pandas as pd
# a=input("Enter your 17-23 length SgRNA sequence:\n")
# b=input("Enter complementary target DNA sequence:\n")
# def user_input(a,b):
#     print(a,len(a),type(a))
#     print(b,len(b),type(b))
# user_input(a,b)
print("Upload your file here:\n")
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
str1 = ""
if file_path:
  with open(file_path, 'r') as file:
    contents = file.read()
    # print(contents)
    data = contents.splitlines()
    for i in range(1,len(data)):
        str1 += data[i]
    # print(str1)
c=input("Enter your 17-23 length SgRNA sequence:\n")
#------------Code to be used in case of collab----------
# from google.colab import files
# uploaded = files.upload()
# str1 = ""
# for key in uploaded.keys():
#   data = uploaded[key].decode("utf-8")
#   data = data.splitlines()
#   for i in range(1,len(data)):
#     str1 += data[i]
# print(str1)
heading = {'sgRNA':[],'Target':[],'Result':[],'Position':[]}
df = pd.DataFrame(heading)
row = 0
for i in range(len(str1)-len(c)+1):
  target = str1[i:len(c)+i]
  df.at[row,'sgRNA'] = c
  df.at[row,'Target'] = target
  min_ind = i+1
  max_ind = len(c) + i
  position = "["+str(min_ind) + "-" + str(max_ind)+"]"
  df.at[row,'Range'] = position
  row += 1
# df.to_excel('sheet.xls', index=False)
df.to_excel('Testing_data.xlsx', index=False)
df.to_csv('Testing_data.csv', index=False)
# df.to_csv('testing.csv', index=False)