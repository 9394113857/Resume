# from flask_ngrok import run_with_ngrok
import pickle

import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)
# run_with_ngrok(app)

# models:
house_price_linear_regression_model = pickle.load(open('house_price_linear_regression.pkl', 'rb'))
iphone_price_linear_regression_model = pickle.load(open('iphone_price_linear_regression.pkl', 'rb'))
single_linear_regression_salary_model = pickle.load(open('single_linear_regression_salary_prediction.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')


# Navigated to home page
@app.route('/homee', methods=['GET'])
def homee():
    return render_template('home.html')


# Navigated to House Price Prediction form:-
@app.route('/house.html', methods=['GET'])
def house():
    return render_template('house.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    area = int(request.form['area'])
    data = np.array([[area]])
    prediction = house_price_linear_regression_model.predict(data)

    return render_template('house.html', prediction_text='House Price could be Rs {}'.format(prediction))


# Navigated to Iphone Price Prediction form:-
@app.route('/phone.html', methods=['GET'])
def iphone():
    return render_template('phone.html')


@app.route('/predict_phone', methods=['POST'])
def predict_phone():
    '''
    For rendering results on HTML GUI
    '''
    version = int(request.form['version'])
    model_version = np.array([[version]])
    iphone_value = iphone_price_linear_regression_model.predict(model_version)

    dollar = iphone_value
    rupees = dollar * 79.71

    return render_template('phone.html', prediction_iphone='Iphone Price could be $ {}'.format(
        iphone_value) + ' And, Iphone Price could be ₹ {}'.format(rupees))

# Navigated to Salary Price Prediction form:-
@app.route('/salary.html', methods=['GET'])
def salary():
    return render_template('salary.html')


@app.route('/predict_salary', methods=['POST'])
def single_linear_salary_prediction():
    '''
    For rendering results on HTML GUI
    '''
    experience = float(request.form['Experience'])
    data = np.array([[experience]])
    prediction = single_linear_regression_salary_model.predict(data)

    return render_template('salary.html', prediction_text='Salary Price could be Rs {}'.format(prediction))


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=1000, debug=True)
    app.run()
