from flask import Flask, render_template, request
import pickle
import numpy as np

# Initialize Flask application
app = Flask(__name__)

# Load the trained machine learning model
model = pickle.load(open("HDI.pkl", "rb"))


# Home Page
@app.route("/")
def home():
    return render_template("home.html")


# Prediction Page
@app.route("/prediction")
def prediction():
    return render_template("indexnew.html")


# Prediction Logic
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get user input
        country = float(request.form["country"])
        life = float(request.form["life"])
        expected = float(request.form["expected"])
        mean = float(request.form["mean"])
        gni = float(request.form["gni"])

        # Convert input into NumPy array
        features = np.array([[country, life, expected, mean, gni]])

        # Predict HDI
        prediction = model.predict(features)[0]

        # Keep prediction within valid HDI range
        prediction = max(0.0, min(1.0, prediction))

        # Determine HDI Category
        if prediction >= 0.800:
            category = "Very High Human Development"
        elif prediction >= 0.700:
            category = "High Human Development"
        elif prediction >= 0.550:
            category = "Medium Human Development"
        else:
            category = "Low Human Development"

        # Display Result
        return render_template(
            "resultnew.html",
            prediction=round(prediction, 3),
            category=category
        )

    except Exception as e:
        return f"Error: {e}"


# Run Flask Application
if __name__ == "__main__":
    app.run(debug=True)