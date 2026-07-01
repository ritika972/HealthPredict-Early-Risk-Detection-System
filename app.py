import streamlit as st
from src.bmi_calculator import calculate_bmi
from src.report_generator import generate_report




menu = st.sidebar.radio(
    "Choose Module",
    [
        "Home",
        "BMI Calculator",
        "Diabetes Prediction",
        "Hypertension Prediction",
        "Dashboard",
        "Report Generation"
    ]
)

# ==========================
# HOME
# ==========================
if menu == "Home":

    st.markdown("""
<div style="
    text-align:center;
    padding:30px;
    border-radius:15px;
    background: linear-gradient(90deg, #1E3C72, #2A5298);
">

<h1 style="color:white; font-size:60px;">
🏥 HealthPredict
</h1>

<h3 style="color:#E8F6FF; font-size:28px;">
Early Risk Detection System
</h3>

<p style="color:white; font-size:18px;">
Predict Health Risks • Get Recommendations • Stay Healthy
</p>

</div>
""", unsafe_allow_html=True)

    st.write("")
    st.write("")

    st.markdown("## 🌟 About HealthPredict")

    st.write("""
    HealthPredict is an intelligent healthcare application that helps users
    identify potential health risks at an early stage using machine learning.
    The system provides risk assessments, health recommendations, dashboards,
    and downloadable PDF reports.
    """)

    st.write("")
    st.markdown("## 🚀 Features")

    col1, col2 = st.columns(2)

    with col1:
        st.success("📏 BMI Calculator")
        st.success("🩸 Diabetes Risk Prediction")
        st.success("❤️ Hypertension Risk Prediction")

    with col2:
        st.success("📊 Health Dashboard")
        st.success("💡 Personalized Recommendations")
        st.success("📄 PDF Report Generation")

    st.write("")
    st.markdown("## 🎯 Benefits")

    st.info("""
    ✔ Early disease detection

    ✔ Better health awareness

    ✔ Preventive healthcare support

    ✔ Easy-to-use interface

    ✔ Instant risk prediction results
    """)

    st.write("")
    st.markdown("## 📖 How to Use")

    st.markdown("""
    1. Select a module from the sidebar.
    2. Enter the required health information.
    3. Click the prediction button.
    4. View your health risk assessment.
    5. Download the generated report if needed.
    """)

    st.write("")
    st.success("💡 Stay Healthy • Stay Informed • Stay Safe")

# ==========================
# BMI CALCULATOR
# ==========================
elif menu == "BMI Calculator":

    st.header("BMI Calculator")

    weight = st.number_input(
        "Weight (kg)",
        min_value=1.0,
        value=60.0,
        key="bmi_weight"
    )

    height = st.number_input(
        "Height (meters)",
        min_value=0.5,
        value=1.70,
        key="bmi_height"
    )

    if st.button("Calculate BMI"):

        bmi, category = calculate_bmi(
            weight,
            height
        )

        st.success(f"BMI: {bmi}")
        st.info(f"Category: {category}")

# ==========================
# DIABETES PREDICTION
# ==========================
elif menu == "Diabetes Prediction":

    st.header("Diabetes Risk Assessment")

    glucose = st.number_input(
        "Glucose Level",
        0,
        300,
        100,
        key="diabetes_glucose"
    )

    bmi = st.number_input(
        "BMI",
        0.0,
        60.0,
        25.0,
        key="diabetes_bmi"
    )

    age = st.number_input(
        "Age",
        1,
        100,
        30,
        key="diabetes_age"
    )

    if st.button("Check Diabetes Risk"):

        score = 0

        if glucose > 140:
            score += 1

        if bmi > 30:
            score += 1

        if age > 45:
            score += 1

        if score == 0:
            st.success("🟢 Low Diabetes Risk")

            st.subheader(" 📋Recommendations")
            st.write("✔ Maintain a balanced diet rich in fruits and vegetables")
            st.write("✔ Continue regular physical activity (30 minutes daily)")
            st.write("✔ Drink adequate water throughout the day")
            st.write("✔ Maintain a healthy body weight")
            st.write("✔ Monitor your health periodically")
            st.write("✔ Get routine health checkups annually")


        elif score == 1:
            st.warning("🟡 Medium Diabetes Risk")
            st.subheader(" 📋Recommendations")
            st.write("✔ Limit sugary foods")
            st.write("✔ Exercise 30 minutes daily")
            st.write("✔ Maintain healthy weight")
            st.write("✔ Increase fruit and vegetable intake")
            st.write("✔ Monitor blood glucose occasionally")
            st.write("✔ Consult a healthcare professional if needed")
        else:
            st.error("🔴 High Diabetes Risk")

            st.subheader(" 📋Recommendations")
            st.write("✔ Limit sugar and refined carbohydrate intake")
            st.write("✔ Follow a healthy, balanced diet")
            st.write("✔ Exercise regularly and maintain an active lifestyle")
            st.write("✔ Monitor blood glucose levels regularly")
            st.write("✔ Maintain a healthy weight")
            st.write("✔ Consult a doctor for further evaluation")
            st.write("✔ Follow prescribed medical advice and treatment")
 
# ==========================
# HYPERTENSION PREDICTION
# ==========================
elif menu == "Hypertension Prediction":

    st.header("Hypertension Risk Assessment")

    systolic = st.number_input(
        "Systolic BP",
        50,
        250,
        120,
        key="systolic"
    )

    diastolic = st.number_input(
        "Diastolic BP",
        30,
        150,
        80,
        key="diastolic"
    )

    age = st.number_input(
        "Age",
        1,
        100,
        30,
        key="bp_age"
    )

    if st.button("Check Blood Pressure Risk"):

        if systolic >= 140 or diastolic >= 90:

            st.error("🔴 High Blood Pressure Risk")

            st.write("✔ Reduce salt intake")
            st.write("✔ Exercise daily")
            st.write("✔ Avoid smoking")
            st.write("✔ Monitor BP regularly")

        elif systolic >= 120:

            st.warning("🟡 Pre-Hypertension")

            st.write("✔ Improve diet")
            st.write("✔ Increase physical activity")

        else:

            st.success("🟢 Normal Blood Pressure")

            st.write("✔ Maintain healthy lifestyle")

# ==========================
# DASHBOARD
# ==========================
elif menu == "Dashboard":

    st.header("📊 Health Dashboard")

    import pandas as pd
    from src.dashboard import show_dashboard

    try:
        df = pd.read_csv("data/diabetes.csv")
        show_dashboard(df)

    except FileNotFoundError:
        st.error("❌ diabetes.csv file not found in data folder")

    except Exception as e:
        st.error(f"❌ Dashboard Error: {e}")

# ==========================
# REPORT GENERATION
# ==========================
elif menu == "Report Generation":

    st.header("📄 Generate Health Report")

    name = st.text_input(
        "Patient Name",
        key="report_name"
    )

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=25,
        key="report_age"
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=1.0,
        value=60.0,
        key="report_weight"
    )

    height = st.number_input(
        "Height (m)",
        min_value=0.5,
        value=1.70,
        key="report_height"
    )

    if st.button("Generate PDF Report"):

        bmi = round(weight / (height ** 2), 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        diabetes_risk = "Low Risk"
        hypertension_risk = "Low Risk"

        pdf_file = generate_report(
            patient_name=name,
            age=age,
            bmi=bmi,
            bmi_category=category,
            diabetes_risk=diabetes_risk,
            hypertension_risk=hypertension_risk
        )

        st.success("✅ Report Generated Successfully")

        with open(pdf_file, "rb") as pdf:
            st.download_button(
                label="📥 Download PDF Report",
                data=pdf,
                file_name=pdf_file,
                mime="application/pdf"
            )