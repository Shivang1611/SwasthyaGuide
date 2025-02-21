import joblib
import streamlit as st
import os
from pathlib import Path

def load_models():
    """Load all required models"""
    try:
        # Get the absolute path to models directory
        current_dir = Path(__file__).parent.parent
        models_dir = current_dir / 'models'
        
        # Create models directory if it doesn't exist
        if not os.path.exists(models_dir):
            os.makedirs(models_dir)
            print(f"Created models directory at {models_dir}")
        
        # Dictionary to store models
        models = {}
        
        # Try to load each model
        try:
            models['heart'] = joblib.load(models_dir / 'heart_model.joblib')
            print("Heart model loaded successfully")
        except:
            print("Heart model not found")
            
        try:
            models['diabetes'] = joblib.load(models_dir / 'diabetes_model.joblib')
            print("Diabetes model loaded successfully")
        except:
            print("Diabetes model not found")
            
        try:
            models['parkinsons'] = joblib.load(models_dir / 'parkinsons_model.joblib')
            print("Parkinsons model loaded successfully")
        except:
            print("Parkinsons model not found")
            
        try:
            models['symptoms'] = joblib.load(models_dir / 'symptoms_model.joblib')
            print("Symptoms model loaded successfully")
        except:
            print("Symptoms model not found")
            
        # Load label encoder and symptom list
        try:
            label_encoder = joblib.load(models_dir / 'label_encoder.joblib')
            symptom_list = joblib.load(models_dir / 'symptom_list.joblib')
            print("Label encoder and symptom list loaded successfully")
        except:
            print("Label encoder or symptom list not found")
            label_encoder = None
            symptom_list = []
        
        return models, label_encoder, symptom_list
        
    except Exception as e:
        print(f"Error in load_models: {str(e)}")
        return {}, None, []