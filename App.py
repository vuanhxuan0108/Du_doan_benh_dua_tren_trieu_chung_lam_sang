import sys
import os

project_path = 'c:\\Users\\84936\\Desktop\\Do_an_TV'

if os.getcwd() != project_path:
    os.chdir(project_path)

if project_path not in sys.path:
    sys.path.append(project_path)

from flask import Flask, render_template, request
import joblib
from tensorflow import keras
from TextPreprocessor import TextPreprocessor
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        symptoms = request.form['symptoms']
        if symptoms.strip() == "":
            return render_template('index.html', error = "Trường này không được để trống")
        else:
            model_lstm = keras.models.load_model(r"model\model.keras")
            encoder = joblib.load(r'model\encoder.joblib')
            label_encoder = joblib.load(r'model\label_encoder.joblib')
            preprocessor = TextPreprocessor(r'dataset/vietnamese.txt')
            sample_text = preprocessor.preprocess_text(symptoms)
            lstm_vector = encoder.transform([sample_text])
            print(lstm_vector)
            if np.sum(lstm_vector) == 0:
                print('Có vẻ như bạn chưa nhập vào 1 triệu chứng?')
            else:
                y_pred_lstm = model_lstm.predict(lstm_vector)
                predictions = y_pred_lstm.argmax(axis=1)
                predictions = label_encoder.inverse_transform([predictions])
                print(predictions)
            link_data = pd.read_excel(r'dataset\link_disease.xlsx')
            link = link_data.loc[link_data['Disease'] == predictions[0], 'Link']
            print(link)
            return render_template('index.html', prediction=predictions[0], link = pd.DataFrame(link).iloc[0, 0])

if __name__ == '__main__':
    app.run(debug=True)
