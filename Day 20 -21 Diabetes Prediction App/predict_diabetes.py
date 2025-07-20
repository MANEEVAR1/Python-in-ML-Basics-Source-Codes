import joblib
import numpy as np

model = joblib.load('diabetes_model.pkl')

def predict_diabetes(input_data):
    features = np.array(input_data).reshape(1, -1)
    prediction = model.predict(features)[0]
    proba = model.predict_proba(features)[0]
    
    return {
        'prediction': int(prediction),
        'probability': {
            'non_diabetic': float(proba[0]),
            'diabetic': float(proba[1])
        }
    }