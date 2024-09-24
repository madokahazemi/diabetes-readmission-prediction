import pickle
import streamlit as st
import pandas as pd
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the preprocessor and model (you'd typically do this once when the app starts)
@st.cache_resource
def load_model_and_preprocessor():
    with open(os.path.join(current_dir, 'simplified_preprocessor.pkl'), 'rb') as f:
        preprocessor = pickle.load(f)
    with open(os.path.join(current_dir, 'simplified_lightgbm_model.pkl'), 'rb') as f:
        model = pickle.load(f)
    with open(os.path.join(current_dir, 'simplified_features.pkl'), 'rb') as f:
        required_features = pickle.load(f)
    with open(os.path.join(current_dir, 'optimal_threshold.pkl'), 'rb') as f:
        optimal_threshold = pickle.load(f)['optimal_threshold']
    return preprocessor, model, required_features, optimal_threshold

preprocessor, model, required_features, optimal_threshold = load_model_and_preprocessor()

def predict_readmission_probability(input_data):
    # Ensure input_data has the correct features
    preprocessed_data = preprocessor.transform(input_data[required_features])
    
    # Get the probability prediction
    probability = model.predict_proba(preprocessed_data)[:, 1]
    
    return probability[0] 



# Input fields
st.title('Hospital Readmission Prediction')

# Age input slider
st.write("""
## Age
""")
input_age = st.slider('Select age', min_value=0, max_value=120, value=65, step=1)

# Diagnosis input dropdown
st.write("""
## Diagnosis
""")
diagnosis_values = ['Digestive', 'Diabetes','Circulatory', 'Musculoskeletal', 'Respiratory', 'Genitourinary', 'Injury', 'Neoplasms',  'Other']
input_diagnosis = st.selectbox('Select diagnosis', diagnosis_values)

# Discharge disposition input dropdown
st.write("""
## Discharge Disposition
""")
discharge_values = ['Home', 'Transfer', 'Other']
input_discharge = st.selectbox('Select discharge disposition', discharge_values)

# Admission type input dropdown
st.write("""
## Admission Type
""")
admission_type_values = ['Emergency', 'Elective','Newborn', 'Other']
input_admission_type = st.selectbox('Select admission type', admission_type_values)

# Admission source input dropdown
st.write("""
## Admission Source
""")
admission_source_values = ['Referral', 'Emergency', 'Transfer', 'Other']
input_admission_source = st.selectbox('Select admission source', admission_source_values)

# Number of lab procedures input slider
st.write("""
## Number of Lab Procedures
""")
input_lab_procedures = st.slider('Select number of lab procedures', min_value=0, max_value=132, value=0, step=1)

# Number of medications input slider
st.write("""
## Number of Medications
""")
input_medications = st.slider('Select number of medications', min_value=0, max_value=132, value=0, step=1)

# Number of inpatient visits input slider
st.write("""
## Number of Inpatient Visits
""")
input_inpatient = st.slider('Select number of inpatient visits', min_value=0, max_value=20, value=0, step=1)

# Number of diagnoses input slider
st.write("""
## Number of Diagnoses
""")
input_diagnoses = st.slider('Select number of diagnoses', min_value=1, max_value=16, value=1, step=1)

# Time in hospital input slider
st.write("""
## Time in Hospital
""")
input_time_in_hospital = st.slider('Select time in hospital (days)', min_value=1, max_value=14, value=1, step=1)

# Prediction button
if st.button('Predict'):
    # Prepare input data
    input_data = {
        'age': input_age,
        'diagnosis': input_diagnosis,
        'discharge_disposition': input_discharge,
        'admission_type': input_admission_type,
        'admission_source': input_admission_source,
        'num_lab_procedures': input_lab_procedures,
        'num_medications': input_medications,
        'number_inpatient': input_inpatient,
        'number_diagnoses': input_diagnoses,
        'time_in_hospital': input_time_in_hospital
    }
    
    # Convert input_data to a DataFrame
    df_input = pd.DataFrame([input_data])
    
    # Debug: Display input data
   # st.write("Input data:", df_input)
    
    # Make prediction (assuming you have this function defined)
    probability = predict_readmission_probability(df_input)
    
    st.write("""
    ## Probability of Readmission
    """)
    st.markdown(f'<h1 style="font-size: 48px; color: #fc4e4b;">{probability:.2%}</h1>', unsafe_allow_html=True)
   
    
    # Provide binary prediction
    #if probability >= optimal_threshold:
        #st.write('Prediction: Likely to be readmitted')
    #else:
        #st.write('Prediction: Not likely to be readmitted')
        
    