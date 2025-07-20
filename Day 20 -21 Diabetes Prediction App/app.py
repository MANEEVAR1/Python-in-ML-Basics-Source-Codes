# app.py
import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load model
model = joblib.load('diabetes_model.pkl')

# Set page config
st.set_page_config(
    page_title="Diabetes Prediction App",
    page_icon="🩺",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6
    }
    .big-font {
        font-size:24px !important;
        font-weight: bold;
    }
    .result-box {
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .diabetic {
        background-color: #ffcccc;
        border-left: 5px solid #ff4b4b;
    }
    .non-diabetic {
        background-color: #ccffcc;
        border-left: 5px solid #4CAF50;
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.title("🩺 Diabetes Prediction App")
st.markdown("""
This app predicts the likelihood of diabetes using the PIMA Indian Diabetes dataset. 
The model is trained on diagnostic measurements including glucose levels, BMI, age, and other health indicators.
""")

# Sidebar for user input
st.sidebar.header("Patient Parameters")
st.sidebar.markdown("Adjust the sliders to input patient health metrics")

# Input fields
pregnancies = st.sidebar.slider('Pregnancies', 0, 17, 3)
glucose = st.sidebar.slider('Glucose Level (mg/dL)', 0, 200, 120)
blood_pressure = st.sidebar.slider('Blood Pressure (mm Hg)', 0, 130, 70)
skin_thickness = st.sidebar.slider('Skin Thickness (mm)', 0, 100, 20)
insulin = st.sidebar.slider('Insulin Level (mu U/ml)', 0, 850, 80)
bmi = st.sidebar.slider('BMI', 0.0, 70.0, 25.0)
dpf = st.sidebar.slider('Diabetes Pedigree Function', 0.0, 2.5, 0.35)
age = st.sidebar.slider('Age', 20, 90, 30)

# Prediction function
def predict():
    input_data = np.array([[
        pregnancies, glucose, blood_pressure, 
        skin_thickness, insulin, bmi, dpf, age
    ]])
    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]
    return prediction, probabilities

# Main content
col1, col2 = st.columns([1, 2])

with col1:
    st.header("Patient Input Summary")
    input_df = pd.DataFrame({
        'Feature': [
            'Pregnancies', 'Glucose', 'Blood Pressure',
            'Skin Thickness', 'Insulin', 'BMI',
            'Diabetes Pedigree', 'Age'
        ],
        'Value': [
            pregnancies, glucose, blood_pressure,
            skin_thickness, insulin, bmi,
            dpf, age
        ]
    })
    st.table(input_df)
    
    if st.button('🔍 Predict Diabetes Risk', use_container_width=True):
        prediction, probabilities = predict()
        non_diabetic_prob = probabilities[0] * 100
        diabetic_prob = probabilities[1] * 100
        
        st.subheader("Prediction Result")
        
        if prediction == 1:
            st.markdown(f"""
            <div class="result-box diabetic">
                <p class="big-font">High Risk of Diabetes</p>
                <p>Probability: {diabetic_prob:.2f}%</p>
            </div>
            """, unsafe_allow_html=True)
            st.warning("Consult a healthcare professional for further evaluation")
        else:
            st.markdown(f"""
            <div class="result-box non-diabetic">
                <p class="big-font">Low Risk of Diabetes</p>
                <p>Probability: {non_diabetic_prob:.2f}%</p>
            </div>
            """, unsafe_allow_html=True)
            st.success("Maintain healthy lifestyle habits")

with col2:
    st.header("Model Insights")
    
    # Feature importance plot
    st.subheader("Feature Importance")
    if hasattr(model, 'coef_'):
        importance = pd.Series(np.abs(model.coef_[0]), index=input_df['Feature'])
    else:  # Random Forest
        importance = pd.Series(model.feature_importances_, index=input_df['Feature'])

    fig, ax = plt.subplots(figsize=(10, 6))
    importance.sort_values().plot(kind='barh', ax=ax, color='skyblue')
    plt.title('Factors Influencing Diabetes Prediction')
    plt.xlabel('Importance Score')
    st.pyplot(fig)
    
    # Glucose vs BMI scatter plot
    st.subheader("Glucose vs BMI Analysis")
    fig2 = plt.figure(figsize=(10, 6))

    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
    names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
         'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
    sns.scatterplot(
        x='Glucose', 
        y='BMI', 
        hue='Outcome', 
        data=pd.read_csv(url, names=names),
        alpha=0.7
    )
    plt.axvline(x=glucose, color='r', linestyle='--')
    plt.axhline(y=bmi, color='r', linestyle='--')
    plt.title('Glucose vs BMI with Patient Position')
    st.pyplot(fig2)

# Footer
st.markdown("---")
st.caption("Model trained on PIMA Indian Diabetes Dataset | Accuracy: 77-80%")

# Run with: streamlit run app.py
