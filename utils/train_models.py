import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os
from pathlib import Path

def train_and_save_models():
    """Train and save all models"""
    try:
        # Get the path to models directory
        current_dir = Path(__file__).parent.parent
        models_dir = current_dir / 'models'
        
        # Create models directory if it doesn't exist
        if not os.path.exists(models_dir):
            os.makedirs(models_dir)
            print(f"Created models directory at {models_dir}")
        
        # Create and save heart disease model
        heart_data = pd.DataFrame({
            'age': np.random.randint(30, 80, 1000),
            'sex': np.random.randint(0, 2, 1000),
            'cp': np.random.randint(0, 4, 1000),
            'target': np.random.randint(0, 2, 1000)
        })
        heart_model = RandomForestClassifier(n_estimators=100, random_state=42)
        heart_model.fit(heart_data.drop('target', axis=1), heart_data['target'])
        joblib.dump(heart_model, models_dir / 'heart_model.joblib')
        print("Heart model saved")
        
        # Create and save diabetes model
        diabetes_data = pd.DataFrame({
            'glucose': np.random.randint(70, 200, 1000),
            'bp': np.random.randint(60, 140, 1000),
            'target': np.random.randint(0, 2, 1000)
        })
        diabetes_model = RandomForestClassifier(n_estimators=100, random_state=42)
        diabetes_model.fit(diabetes_data.drop('target', axis=1), diabetes_data['target'])
        joblib.dump(diabetes_model, models_dir / 'diabetes_model.joblib')
        print("Diabetes model saved")
        
        # Create and save Parkinson's model
        parkinsons_data = pd.DataFrame({
            'tremor': np.random.randint(0, 10, 1000),
            'rigidity': np.random.randint(0, 10, 1000),
            'target': np.random.randint(0, 2, 1000)
        })
        parkinsons_model = RandomForestClassifier(n_estimators=100, random_state=42)
        parkinsons_model.fit(parkinsons_data.drop('target', axis=1), parkinsons_data['target'])
        joblib.dump(parkinsons_model, models_dir / 'parkinsons_model.joblib')
        print("Parkinsons model saved")
        
        # Create and save symptoms model and related data
        symptoms = ['fever', 'cough', 'headache', 'fatigue', 'nausea']
        diseases = ['cold', 'flu', 'covid']
        
        # Save symptom list
        joblib.dump(symptoms, models_dir / 'symptom_list.joblib')
        
        # Create and save label encoder
        le = LabelEncoder()
        le.fit(diseases)
        joblib.dump(le, models_dir / 'label_encoder.joblib')
        
        # Create symptoms model
        symptoms_data = pd.DataFrame({
            'symptom': np.random.choice(symptoms, 1000),
            'disease': np.random.choice(diseases, 1000)
        })
        X = pd.get_dummies(symptoms_data['symptom'])
        y = le.transform(symptoms_data['disease'])
        
        symptoms_model = RandomForestClassifier(n_estimators=100, random_state=42)
        symptoms_model.fit(X, y)
        joblib.dump(symptoms_model, models_dir / 'symptoms_model.joblib')
        print("Symptoms model and related data saved")
        
        print("All models trained and saved successfully!")
        return True
        
    except Exception as e:
        print(f"Error in train_and_save_models: {str(e)}")
        return False

if __name__ == "__main__":
    train_and_save_models()