<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> de2a4a5 (Repo-initialised)
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, Dict, Any
import numpy as np
import uvicorn
from model_loader import load_models  # Updated import
<<<<<<< HEAD


app = FastAPI()

class HeartDiseaseInput(BaseModel):
    age: int
    sex: str
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

class ParkinsonsInput(BaseModel):
    age: int
    gender: str
    ethnicity: int
    bmi: float
    smoking: int
    alcohol: float
    physical_activity: float
    diet_quality: float
    sleep_quality: float
    family_history: int
    brain_injury: int
    diabetes: int
    depression: int
    stroke: int
    systolic_bp: int
    diastolic_bp: int
    cholesterol: float
    tremor: int
    rigidity: int
    bradykinesia: int
    postural_instability: int
    speech_problems: int
    sleep_disorders: int
    constipation: int

class DiabetesInput(BaseModel):
    pregnancies: int
    glucose: int
    blood_pressure: int
    skin_thickness: int
    insulin: int
    bmi: float
    dpf: float
    age: int

async def predict_diabetes(data: DiabetesInput) -> str:
    input_data = np.array([[data.pregnancies, data.glucose, data.blood_pressure, data.skin_thickness, 
                            data.insulin, data.bmi, data.dpf, data.age]])
    prediction = models["diabetes_best"].predict(input_data)
    return "Positive for Diabetes. Consult a doctor!" if prediction[0] == 1 else "No Diabetes detected."

async def predict_parkinsons(data: ParkinsonsInput) -> str:
    input_data = np.array([[data.age, 1 if data.gender == "Male" else 0, data.ethnicity, data.bmi, 
                            data.smoking, data.alcohol, data.physical_activity, data.diet_quality, 
                            data.sleep_quality, data.family_history, data.brain_injury, data.diabetes, 
                            data.depression, data.stroke, data.systolic_bp, data.diastolic_bp, 
                            data.cholesterol, data.tremor, data.rigidity, data.bradykinesia, 
                            data.postural_instability, data.speech_problems, data.sleep_disorders, 
                            data.constipation]])
    prediction = models["parkinsons"].predict(input_data)
    return "Parkinson's Detected. Consult a specialist!" if prediction[0] == 1 else "No Parkinson's detected."

async def predict_heart_disease(data: HeartDiseaseInput) -> str:
    input_data = np.array([[data.age, 1 if data.sex == "Male" else 0, data.cp, data.trestbps, 
                            data.chol, data.fbs, data.restecg, data.thalach, data.exang, 
                            data.oldpeak, data.slope, data.ca, data.thal]])
    prediction = models["heart"].predict(input_data)
    return "Has Heart Disease. Consult a doctor!" if prediction[0] == 1 else "No Heart Disease detected."

class InputData(BaseModel):
    prediction_type: str
    prediction_data: Dict[str, Any]

@app.post("/api")
async def process_data(data: InputData):
    if data.prediction_type == "heart_disease":
        prediction = await predict_heart_disease(HeartDiseaseInput(**data.prediction_data))
    elif data.prediction_type == "parkinsons":
        prediction = await predict_parkinsons(ParkinsonsInput(**data.prediction_data))
    elif data.prediction_type == "diabetes":
        prediction = await predict_diabetes(DiabetesInput(**data.prediction_data))
    else:
        raise HTTPException(status_code=400, detail="Invalid prediction type")
    
    return JSONResponse(content={"prediction": prediction})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
=======
import streamlit as st
import requests
import os
import dotenv
=======
>>>>>>> de2a4a5 (Repo-initialised)


app = FastAPI()

class HeartDiseaseInput(BaseModel):
    age: int
    sex: str
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

class ParkinsonsInput(BaseModel):
    age: int
    gender: str
    ethnicity: int
    bmi: float
    smoking: int
    alcohol: float
    physical_activity: float
    diet_quality: float
    sleep_quality: float
    family_history: int
    brain_injury: int
    diabetes: int
    depression: int
    stroke: int
    systolic_bp: int
    diastolic_bp: int
    cholesterol: float
    tremor: int
    rigidity: int
    bradykinesia: int
    postural_instability: int
    speech_problems: int
    sleep_disorders: int
    constipation: int

class DiabetesInput(BaseModel):
    pregnancies: int
    glucose: int
    blood_pressure: int
    skin_thickness: int
    insulin: int
    bmi: float
    dpf: float
    age: int

async def predict_diabetes(data: DiabetesInput) -> str:
    input_data = np.array([[data.pregnancies, data.glucose, data.blood_pressure, data.skin_thickness, 
                            data.insulin, data.bmi, data.dpf, data.age]])
    prediction = models["diabetes_best"].predict(input_data)
    return "Positive for Diabetes. Consult a doctor!" if prediction[0] == 1 else "No Diabetes detected."

async def predict_parkinsons(data: ParkinsonsInput) -> str:
    input_data = np.array([[data.age, 1 if data.gender == "Male" else 0, data.ethnicity, data.bmi, 
                            data.smoking, data.alcohol, data.physical_activity, data.diet_quality, 
                            data.sleep_quality, data.family_history, data.brain_injury, data.diabetes, 
                            data.depression, data.stroke, data.systolic_bp, data.diastolic_bp, 
                            data.cholesterol, data.tremor, data.rigidity, data.bradykinesia, 
                            data.postural_instability, data.speech_problems, data.sleep_disorders, 
                            data.constipation]])
    prediction = models["parkinsons"].predict(input_data)
    return "Parkinson's Detected. Consult a specialist!" if prediction[0] == 1 else "No Parkinson's detected."

async def predict_heart_disease(data: HeartDiseaseInput) -> str:
    input_data = np.array([[data.age, 1 if data.sex == "Male" else 0, data.cp, data.trestbps, 
                            data.chol, data.fbs, data.restecg, data.thalach, data.exang, 
                            data.oldpeak, data.slope, data.ca, data.thal]])
    prediction = models["heart"].predict(input_data)
    return "Has Heart Disease. Consult a doctor!" if prediction[0] == 1 else "No Heart Disease detected."

class InputData(BaseModel):
    prediction_type: str
    prediction_data: Dict[str, Any]

@app.post("/api")
async def process_data(data: InputData):
    if data.prediction_type == "heart_disease":
        prediction = await predict_heart_disease(HeartDiseaseInput(**data.prediction_data))
    elif data.prediction_type == "parkinsons":
        prediction = await predict_parkinsons(ParkinsonsInput(**data.prediction_data))
    elif data.prediction_type == "diabetes":
        prediction = await predict_diabetes(DiabetesInput(**data.prediction_data))
    else:
<<<<<<< HEAD
        st.warning("Message cannot be empty")
>>>>>>> a9cfe88 (hellow)
=======
        raise HTTPException(status_code=400, detail="Invalid prediction type")
    
    return JSONResponse(content={"prediction": prediction})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
>>>>>>> de2a4a5 (Repo-initialised)
