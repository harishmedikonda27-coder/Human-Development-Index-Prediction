# Human Development Index (HDI) Prediction using Machine Learning and Flask

## 📌 Project Overview

The Human Development Index (HDI) Prediction System is a Machine Learning-based web application that predicts the Human Development Index (HDI) score of a country based on important socio-economic indicators.

The project uses a Linear Regression model trained on the United Nations Development Programme (UNDP) Human Development dataset. A Flask web application is developed to provide an interactive interface where users can enter country details and instantly receive the predicted HDI score along with its development category.

---

## 🎯 Objectives

- Predict Human Development Index (HDI) values using Machine Learning.
- Analyze the relationship between education, life expectancy, income, and HDI.
- Build an interactive web application using Flask.
- Deploy the trained model for real-time predictions.

---

## 🚀 Features

- Data preprocessing and cleaning
- Data visualization using Matplotlib and Seaborn
- Linear Regression model training
- Model evaluation using R² Score
- Model serialization using Pickle
- Flask-based web interface
- Real-time HDI prediction
- HDI category classification

---

## 🛠 Technologies Used

### Programming Language

- Python 3

### Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Flask
- Pickle

### Tools

- Visual Studio Code
- Jupyter Notebook
- Git
- GitHub

---

## 📂 Project Structure

```
Human Development Index/
│
├── Dataset/
│   └── HDI.csv
│
├── Flask/
│   ├── app.py
│   ├── HDI.pkl
│   └── templates/
│       ├── home.html
│       ├── indexnew.html
│       └── resultnew.html
│
├── Training/
│   ├── HunDevIndex.ipynb
│   └── columns.txt
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📊 Dataset

The dataset contains Human Development Index indicators published by the United Nations Development Programme (UNDP).

Selected Features:

- Country
- Life Expectancy at Birth (2021)
- Expected Years of Schooling (2021)
- Mean Years of Schooling (2021)
- Gross National Income Per Capita (2021)

Target Variable:

- Human Development Index (2021)

---

## 🤖 Machine Learning Workflow

1. Import Dataset
2. Data Understanding
3. Data Visualization
4. Data Preprocessing
5. Label Encoding
6. Train-Test Split
7. Linear Regression Model Training
8. Model Evaluation
9. Save Model using Pickle
10. Flask Web Application Development

---

## 📈 Model Performance

Algorithm Used:

- Linear Regression

Evaluation Metric:

- R² Score

Model Accuracy:

```
R² Score = 0.9745
```

The model explains approximately **97.45%** of the variance in the HDI values, indicating strong predictive performance.

---

## 🌐 Flask Application

The web application consists of three pages:

### Home Page

Provides a brief introduction to the Human Development Index prediction system.

### Prediction Page

Users enter:

- Country
- Life Expectancy
- Expected Years of Schooling
- Mean Years of Schooling
- Gross National Income Per Capita

The application predicts the HDI score.

### Result Page

Displays:

- Predicted HDI Score
- Human Development Category

Categories:

- Very High Human Development
- High Human Development
- Medium Human Development
- Low Human Development

---

## ▶️ How to Run the Project

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Human-Development-Index-Prediction.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Flask application

```bash
cd Flask
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 📸 Application Screenshots

Add screenshots here after uploading.

- Home Page
- Prediction Page
- Result Page

---

## 🔮 Future Enhancements

- Deploy the application on Render
- Improve prediction accuracy using advanced regression algorithms
- Add interactive data visualizations
- Support multiple machine learning models
- Enhance the user interface

---

## 👨‍💻 Author

**Hareesh Medikonda**

B.Tech CSE (Data Science)

---

## 📜 License

This project is developed for educational and internship purposes.