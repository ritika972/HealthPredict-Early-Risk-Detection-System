# HealthPredict-Early-Risk-Detection-System
HealthPredict is a Machine Learning-based healthcare application that predicts diabetes risk, calculates BMI, provides personalized health recommendations, and generates downloadable PDF health reports using Python and Streamlit.
# 🩺 HealthPredict – Early Risk Detection System

HealthPredict is a Machine Learning-based healthcare application developed using Python and Streamlit. It helps users assess their diabetes risk by analyzing health parameters such as glucose level, blood pressure, BMI, insulin, and age. The system also provides personalized health recommendations and generates a downloadable PDF report.

---

## 🚀 Features

- Diabetes Risk Prediction using Machine Learning
- BMI Calculator
- Personalized Health Recommendations
- Interactive Streamlit Dashboard
- PDF Health Report Generation
- User-Friendly Interface
- Real-time Prediction

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Plotly
- ReportLab
- Joblib

---

## 📂 Project Structure

```
HealthPredict/
│── Data/
│── src/
│── app.py
│── model.pkl
│── scaler.pkl
│── requirements.txt
│── README.md
```

---

## 📊 Dataset Features

The model uses the following health parameters:

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

### Target Variable

- 0 → Non-Diabetic
- 1 → Diabetic

---

## ⚙️ How It Works

1. User enters health details.
2. BMI is calculated.
3. Data is preprocessed and scaled.
4. The Machine Learning model predicts diabetes risk.
5. Personalized recommendations are displayed.
6. A downloadable PDF health report is generated.

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/HealthPredict.git
```

Go to project folder

```bash
cd HealthPredict
```

Install required libraries

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📸 Output

The application provides:

- Health Risk Prediction
- BMI Status
- Confidence Display
- Personalized Recommendations
- Downloadable PDF Report

---

## 📈 Future Improvements

- Support Multiple Diseases
- Email PDF Reports
- Doctor Consultation Integration
- Cloud Deployment
- Improved Machine Learning Models
- Real-time Health Monitoring

---

## 👩‍💻 Author

**Ritika Gorakh Kale**

MSc Data Science Student
