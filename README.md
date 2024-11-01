# Gold-Price-Prediction-Using-Ensemble-Learning-Techniques

This project is a web application built using Flask to predict gold prices based on selected input features. The model is trained using machine learning, specifically a Random Forest model, to predict the GLD (gold price) value based on SPX, SLV, USO, and EUR/USD values. This application loads the trained model and provides a simple web interface for users to input values and get the predicted gold price.

Project Structure
front_end.py: The main Flask application file that handles routes and prediction logic.
gld_price_data.csv: The dataset used to train the model, containing historical data for gold prices and related financial indicators.
Main.ipynb: A Jupyter Notebook containing the code for data analysis, model training, and initial exploration of the dataset.
Requirements
Before running the project, make sure you have the following installed:

Python 3.8 or higher
Flask
Joblib
Pandas
Scikit-learn
You can install the required Python libraries using:

bash
Copy code
pip install -r requirements.txt
How to Run the Application
Prepare the Model: Ensure that your trained model (random_forest_model.joblib) is saved in the same directory as front_end.py.

Run the Flask Application:

In your terminal, navigate to the directory containing front_end.py.
Run the following command:
bash
Copy code
python front_end.py
The application will start on http://127.0.0.1:5000.
Access the Web Application:

Open your web browser and go to http://127.0.0.1:5000.
You will see an input form where you can enter values for:
SPX (S&P 500 Index)
SLV (Silver Price)
USO (Oil Price)
EUR/USD (Euro to USD exchange rate)
Submit the form to get the predicted gold price.
Code Explanation
1. front_end.py
This file contains the Flask code to create the web application.

Routes:
@app.route('/'): The home route that renders index.html, which is the form for input values.
@app.route('/predict', methods=['POST']): The prediction route. It:
Retrieves input values from the form.
Passes the values to the trained model to predict the gold price.
Renders the result.html template with the prediction result.
2. Main.ipynb
This notebook contains data analysis and model training code. The main steps include:

Loading and Exploring Data: Load gld_price_data.csv and perform basic exploratory data analysis.
Feature Selection: Selecting SPX, SLV, USO, and EUR/USD as predictor variables.
Model Training: Using a Random Forest model to predict GLD.
Model Exporting: Saving the trained model as random_forest_model.joblib.
3. gld_price_data.csv
This is the CSV file with historical data that includes:

SPX: S&P 500 Index values.
SLV: Silver prices.
USO: Oil prices.
EUR/USD: Exchange rate of Euro to USD.
GLD: Gold prices (the target variable for prediction).
Usage Example
Here is an example of values you can use to test the application:

SPX: 4300.25
SLV: 22.15
USO: 70.35
EUR/USD: 1.12
Entering these values and submitting the form will yield a prediction for the gold price (GLD)
