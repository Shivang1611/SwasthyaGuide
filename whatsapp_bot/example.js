# Example JavaScript code to call this API for each prediction type

// Heart Disease Prediction
fetch('http://localhost:8000/api', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        prediction_type: 'heart_disease',
        prediction_data: {
            age: 45,
            sex: 'Male',
            cp: 2,
            trestbps: 130,
            chol: 250,
            fbs: 0,
            restecg: 1,
            thalach: 150,
            exang: 0,
            oldpeak: 1.5,
            slope: 1,
            ca: 0,
            thal: 2
        }
    })
})
.then(response => response.json())
.then(data => console.log('Heart Disease Prediction:', data))
.catch((error) => console.error('Error:', error));

// Parkinson's Disease Prediction
fetch('http://localhost:8000/api', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        prediction_type: 'parkinsons',
        prediction_data: {
            age: 60,
            gender: 'Male',
            ethnicity: 1,
            bmi: 25.0,
            smoking: 0,
            alcohol: 0.0,
            physical_activity: 1.0,
            diet_quality: 1.0,
            sleep_quality: 1.0,
            family_history: 0,
            brain_injury: 0,
            diabetes: 0,
            depression: 0,
            stroke: 0,
            systolic_bp: 120,
            diastolic_bp: 80,
            cholesterol: 200.0,
            tremor: 0,
            rigidity: 0,
            bradykinesia: 0,
            postural_instability: 0,
            speech_problems: 0,
            sleep_disorders: 0,
            constipation: 0
        }
    })
})
.then(response => response.json())
.then(data => console.log("Parkinson's Disease Prediction:", data))
.catch((error) => console.error('Error:', error));

// Diabetes Prediction
fetch('http://localhost:8000/api', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        prediction_type: 'diabetes',
        prediction_data: {
            pregnancies: 2,
            glucose: 150,
            blood_pressure: 80,
            skin_thickness: 20,
            insulin: 100,
            bmi: 30.0,
            dpf: 0.5,
            age: 35
        }
    })
})
.then(response => response.json())
.then(data => console.log('Diabetes Prediction:', data))
.catch((error) => console.error('Error:', error));