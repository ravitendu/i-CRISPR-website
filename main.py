import pandas as pd
import openpyxl
from flask import Flask, render_template, request, Response, redirect, url_for, send_from_directory


from utils.User_input import user_input_handling

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/user_input', methods=['GET','POST'])
# getting user input from front end
def user_input():
    sgRNA = request.form.get('sgRNA')
    target_DNA = request.form.get('target_DNA')
    filename = request.files['filename']
    model = request.form.get('model')

    if target_DNA:
        user_input_handling(sgRNA, target_DNA, model)

    if not target_DNA:
        str1 = ""
        contents = filename.read()
        data = contents.splitlines()
        for i in range(1,len(data)):
            str1 += data[i].decode()
        user_input_handling(sgRNA, str1, model)
    return redirect(url_for('show_result', type=model))

@app.route('/result', methods=['GET', 'POST'])
def show_result():
    model = request.args.get('type')
    arr = []

    if model == 'Machine Learning':
        file = './utils/i-CRISPR(ML)_result.csv'
    
    elif model == 'Deep Learning':
        file = './utils/i-CRISPR(DL)_result.xlsx'
        output_file = './utils/temp.csv'
        df = pd.read_excel(file, header=None)
        df.to_csv(output_file, index=False, header=False)
        file = './utils/temp.csv'

    user_data = pd.read_csv(file, header=None).to_dict('index')
    arr = list(user_data.values())[1:]    
    return render_template('result.html', data=arr, type=model)

@app.route("/download/<type>")
def download_file(type):
    print(type)
    path = './utils'

    if type == 'Deep Learning':
        file_name = 'i-CRISPR(DL)_result.csv'
    elif type == "Machine Learning":
        file_name = 'i-CRISPR(ML)_result.csv'
    
    return send_from_directory(path, file_name, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)