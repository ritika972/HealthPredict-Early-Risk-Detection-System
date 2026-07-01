import streamlit as st
import plotly.express as px

st.markdown("""
<style>
.metric-card{
    background-color:#f0f8ff;
    padding:15px;
    border-radius:15px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.1);
    text-align:center;
}
.main-title{
    text-align:center;
    color:#0066cc;
}
</style>
""", unsafe_allow_html=True)



def show_dashboard(df):

    # ==========================
    # DATASET PREVIEW
    # ==========================

    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head())

    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

    st.divider()

    # ==========================
    # KEY METRICS
    # ==========================

    st.subheader("📌 Key Health Metrics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Patients", len(df))

    if "Age" in df.columns:
        col2.metric("Average Age", round(df["Age"].mean(), 2))

    if "BMI" in df.columns:
        col3.metric("Average BMI", round(df["BMI"].mean(), 2))

    if "Glucose" in df.columns:
        col4.metric("Average Glucose", round(df["Glucose"].mean(), 2))

    st.divider()

    # ==========================
    # BMI DISTRIBUTION
    # ==========================

    if "BMI" in df.columns:

        st.subheader("⚖️ BMI Distribution")

        def bmi_category(bmi):
            if bmi < 18.5:
                return "Underweight"
            elif bmi < 25:
                return "Normal"
            elif bmi < 30:
                return "Overweight"
            else:
                return "Obese"

        temp_df = df.copy()
        temp_df["BMI Category"] = temp_df["BMI"].apply(bmi_category)

        bmi_chart = px.pie(
            temp_df,
            names="BMI Category",
            title="BMI Categories"
        )

        st.plotly_chart(bmi_chart, use_container_width=True)

    # ==========================
    # GLUCOSE DISTRIBUTION
    # ==========================

    if "Glucose" in df.columns:

        st.subheader("📈 Glucose Distribution")

        glucose_chart = px.histogram(
            df,
            x="Glucose",
            nbins=20,
            title="Glucose Levels"
        )

        st.plotly_chart(glucose_chart, use_container_width=True)

    # ==========================
    # BLOOD PRESSURE
    # ==========================

    if "BloodPressure" in df.columns:

        st.subheader("❤️ Blood Pressure Analysis")

        bp_chart = px.histogram(
            df,
            x="BloodPressure",
            nbins=20,
            title="Blood Pressure Distribution"
        )

        st.plotly_chart(bp_chart, use_container_width=True)

    

    # ==========================
    # RECOMMENDATIONS
    # ==========================

    st.subheader("📝 Recommendations")

    st.success("Exercise at least 30 minutes daily")
    st.success("Maintain a healthy BMI")
    st.success("Reduce sugar intake")
    st.success("Drink enough water")
    st.success("Monitor blood pressure regularly")
    st.success("Get regular health checkups")