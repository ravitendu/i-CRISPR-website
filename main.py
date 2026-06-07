import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

from utils.User_input import user_input_handling

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/user_input', methods=['GET', 'POST'])
def user_input():

    sgRNA = request.form.get('sgRNA')
    target_DNA = request.form.get('target_DNA')
    filename = request.files['filename']

    # Machine Learning is the only model now
    model = "Machine Learning"

    if target_DNA:
        user_input_handling(sgRNA, target_DNA, model)

    else:
        str1 = ""
        contents = filename.read()
        data = contents.splitlines()

        for i in range(1, len(data)):
            str1 += data[i].decode()

        user_input_handling(sgRNA, str1, model)

    return redirect(url_for('show_result'))


@app.route('/result', methods=['GET', 'POST'])
def show_result():

    file = './utils/i-CRISPR(ML)_result.csv'

    user_data = pd.read_csv(file, header=None).to_dict('index')
    arr = list(user_data.values())[1:]

    return render_template('result.html',
                           data=arr,
                           type="Machine Learning")


@app.route("/download")
def download_file():

    path = './utils'
    file_name = 'i-CRISPR(ML)_result.csv'

    return send_from_directory(path,
                               file_name,
                               as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)