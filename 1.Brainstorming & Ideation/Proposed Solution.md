# Proposed Solution

The proposed solution is to build a Machine Learning-based web application that predicts the Human Development Index (HDI) score from key socio-economic indicators.

## Input Parameters

* Country
* Life Expectancy
* Expected Years of Schooling
* Mean Years of Schooling
* Gross National Income (GNI) per Capita

## Process

1. Collect and preprocess the dataset.
2. Train a Linear Regression model.
3. Save the trained model using Pickle.
4. Integrate the model into a Flask web application.
5. Accept user inputs through an HTML interface.
6. Predict the HDI score.
7. Display the predicted score and corresponding Human Development category.

## Expected Outcome

The system provides an instant prediction of the HDI score and classifies it into one of the following categories:

* Very High Human Development
* High Human Development
* Medium Human Development
* Low Human Development

The application serves as an educational and analytical tool for understanding human development indicators.
