# System Architecture

The Human Development Index (HDI) Prediction System follows a simple Machine Learning architecture.

## Components

### User Interface

* Home Page
* Prediction Page
* Result Page

### Flask Backend

* Receives user input.
* Validates the entered values.
* Sends data to the trained Machine Learning model.

### Machine Learning Model

* Linear Regression model trained using the HDI dataset.
* Predicts the Human Development Index (HDI) score.

### Output Module

* Displays the predicted HDI score.
* Displays the corresponding Human Development category.

## Architecture Flow

User → HTML Forms → Flask Application → Machine Learning Model → Prediction Result → User
