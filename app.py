import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

with open(r'C:\Users\user\Documents\Fetal AI\fetal_health.pkl', 'rb') as file:
    loaded_model = pickle.load(file)
    print(f"Loaded model type: {type(loaded_model)}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        accelerations = float(request.form['acc'])
        prolongued_decelerations = float(request.form['pd'])
        abnormal_short_term_variability = float(request.form['astv'])
        percentage_of_time_with_abnormal_long_term_variability = float(request.form['pot'])
        mean_value_of_long_term_variability = float(request.form['mv'])
        histogram_mode = float(request.form['hm'])
        histogram_median = float(request.form['hmed'])
        histogram_variance = float(request.form['hv'])
    
    except ValueError:
        return f"Error: Invalid input. Please enter numeric values for all fields."
    
    input_data = [[
        accelerations,
        prolongued_decelerations,
        abnormal_short_term_variability,
        percentage_of_time_with_abnormal_long_term_variability,
        mean_value_of_long_term_variability,
        histogram_mode,
        histogram_median,
        histogram_variance
    ]]
    prediction = loaded_model.predict(input_data)[0]

    if prediction == 1:
        result = "Normal"
    elif prediction == 2:
        result = "Suspect"
    elif prediction == 3:
        result = "Pathological"
    else:
        result = "Unknown"
    
    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
