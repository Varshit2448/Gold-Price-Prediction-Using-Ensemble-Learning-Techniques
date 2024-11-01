from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('random_forest_model.joblib')  # Update the path if needed

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values for spx, slv, uso, and eur/usd from the form
        spx = float(request.form['spx'])
        slv = float(request.form['slv'])
        uso = float(request.form['uso'])
        eur_usd = float(request.form['eur_usd'])
        
        # Arrange inputs into the model's expected format
        features = np.array([[spx, slv, uso, eur_usd]])
        
        # Make prediction using the model
        gld_prediction = model.predict(features)
        
        # Return the prediction result
        return render_template('result.html', prediction=round(gld_prediction[0], 2))
    
    except Exception as e:
        # Display error message if something goes wrong
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
