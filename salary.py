from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
single_linear_regression_salary_prediction_model = pickle.load(open('single_linear_regression_salary_prediction.pkl', 'rb'))
multi_linear_regression_salary_prediction_model = pickle.load(open('multi_linear_regression_salary_prediction.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('homee.html')


# Navigated to home page
@app.route('/homee', methods=['GET'])
def homee():
    return render_template('homee.html')


###

@app.route('/single_linear.html')
def single_linear():
    return render_template('single_linear.html')


@app.route('/predict_single_linear', methods=['POST'])
def predict_single_linear():
    experience = float(request.form['experience'])
    prediction = single_linear_regression_salary_prediction_model.predict([[experience]])
    return 'The predicted salary is: $' + str(round(prediction[0], 2))


@app.route('/multi_linear.html')
def multi_linear():
    return render_template('multi_linear.html')


@app.route('/predict_multi_linear', methods=['POST'])
def predict_multi_linear():
    experience = float(request.form['experience'])
    test_score = float(request.form['test_score'])
    interview_score = float(request.form['interview_score'])
    prediction = multi_linear_regression_salary_prediction_model.predict([[experience, test_score, interview_score]])
    return 'The predicted salary is: $' + str(round(prediction[0], 2))


if __name__ == '__main__':
    app.run(debug=True)
