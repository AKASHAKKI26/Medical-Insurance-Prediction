# ⚕️ Medical Insurance Charges Prediction

Link --> https://medical-insurance-prediction-eiskolcbzryydupzjdgvep.streamlit.app/

## 📌 Project Overview

This project predicts **medical insurance charges** based on user inputs such as age, BMI, number of children, and smoking status.
The model was trained using a **Linear Regression algorithm** and deployed with a **Streamlit web interface**.

The application allows users to enter health and demographic details and get an estimated insurance charge instantly.

---

## 📊 Features

* Predict medical insurance charges
* Simple and interactive Streamlit web interface
* Uses a trained Machine Learning model
* Real-time predictions

---

## 🧠 Machine Learning Model

The prediction model was built using **Linear Regression** from Scikit-learn.

### Input Features

* Age
* BMI
* Number of Children
* Smoker (Yes / No)
* Interaction Feature (Smoker × BMI)

### Target Variable

* Insurance Charges

---

## 📂 Project Structure

```
Medical-Insurance-Prediction
│
├── insurance.csv            # Dataset
├── prediction.ipynb         # Model training notebook
├── insurance_model.pkl      # Trained ML model
├── interface.py             # Streamlit application
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/medical-insurance-prediction.git
cd medical-insurance-prediction
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Streamlit App

```
streamlit run interface.py
```

The app will open in your browser at:

```
http://localhost:8501
```

---

## 🖥️ Application Interface

The application asks the user to provide:

* Age
* BMI
* Number of Children
* Smoking Status

Then it predicts the **estimated medical insurance charges**.

---

## 📦 Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* Pickle

---

## 📈 Future Improvements

* Add region and gender features
* Use advanced ML models (Random Forest / XGBoost)
* Improve UI design
* Deploy on Streamlit Cloud or AWS

---

## 👨‍💻 Author

Akash B
