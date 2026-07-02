# Design Summary

The Human Development Index Prediction System is designed using a modular architecture.

The frontend is developed using HTML and CSS to provide a simple and responsive user interface.

The backend is implemented using the Flask framework, which handles routing, input validation, and communication with the Machine Learning model.

A Linear Regression model is trained using the Human Development Index dataset and saved as a Pickle (.pkl) file. During prediction, the Flask application loads the trained model, processes the user inputs, predicts the HDI score, and returns the result to the user.

This modular design ensures simplicity, maintainability, and easy future enhancements.
