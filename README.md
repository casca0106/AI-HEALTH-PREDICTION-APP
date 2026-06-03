# AI Health Prediction App

## Overview

The AI Health Prediction App is a machine learning-powered healthcare management system built using Python, Streamlit, SQLite, and Scikit-learn.

The application allows users to:

* Add patient health records
* Predict patient risk levels using a trained ML model
* View and manage patient records
* Search and filter patients
* Visualize patient risk analytics
* Export patient data as CSV

This project demonstrates the integration of:

* Machine Learning
* Data Visualization
* Database Management
* CRUD Operations
* Interactive Dashboard Development

---

# Features

## Patient Management

* Add new patients
* View all patient records
* Update patient information
* Delete patient records

---

## AI/ML Prediction System

The application uses a Logistic Regression machine learning model to predict patient risk levels based on:

* Glucose
* Haemoglobin
* Cholesterol

Predictions include:

* Low Risk
* Medium Risk
* High Risk

---

## Dashboard Analytics

Interactive dashboard containing:

* Total patient count
* High-risk patient count
* Medium-risk patient count
* Low-risk patient count
* Bar chart visualization
* Pie chart visualization

---

## Search & Filtering

Users can:

* Search patients by name
* Filter patients by risk category

---

## Data Export

Patient records can be downloaded as a CSV file for reporting and analysis purposes.

---

# Technologies Used

* Python
* Streamlit
* SQLite
* Pandas
* Matplotlib
* Scikit-learn

---

# Project Structure

```plaintext
AI-Health-Prediction-App/
│
├── app.py
├── database.db
├── model.pkl
│
├── dataset/
│   └── health_data.csv
│
├── models/
│   ├── train_model.py
│   └── predict.py
│
├── utils/
│   ├── db.py
│   └── validation.py
```

---

# Machine Learning Model

The application uses:

* Logistic Regression

The model was trained using healthcare-related features and saved using:

* Joblib

The trained model is loaded dynamically during runtime for live predictions.

---

# How to Run the Project

## Step 1: Clone the Repository

```bash
git clone <your-github-repo-link>
```

---

## Step 2: Navigate to the Project Folder

```bash
cd AI-Health-Prediction-App
```

---

## Step 3: Install Required Packages

```bash
pip install streamlit pandas matplotlib scikit-learn
```

---

## Step 4: Run the Application

```bash
streamlit run app.py
```

---

# Future Improvements

Possible future enhancements:

* User Authentication
* Better UI Styling
* Deployment on Streamlit Cloud
* Advanced ML Models
* PDF Report Generation
* Cloud Database Integration

---

# Author

Tanmayee Narendra Chaudhari

B.Tech Data Science Graduate

---

# Conclusion

This project demonstrates how machine learning can be integrated with modern web-based dashboards to create interactive healthcare management systems.

The application combines:

* Machine Learning
* Data Analytics
* Visualization
* Database Management
* Interactive User Interfaces

into a complete end-to-end data science project.
