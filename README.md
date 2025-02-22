
# SwasthyaGuide - Your Personal Health Assistant

#### [Live Here](https://swasthyaguide.streamlit.app/)

SwasthyaGuide is a Streamlit-based health app designed to provide quick and easy access to vital health information and services.  It offers a range of features, from disease prediction and first aid information to details on government healthcare policies and a WhatsApp chatbot integration.

## Table of Contents

* [Introduction](#introduction)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)


## Introduction

SwasthyaGuide aims to empower users with the information they need to manage their health proactively.  Whether you're looking for first aid advice, trying to understand potential symptoms, or seeking information on government healthcare programs, SwasthyaGuide is here to help.  The app combines the power of machine learning with a user-friendly interface to provide a valuable resource for everyone.

## Features

* **WhatsApp Chatbot:** Interact with a chatbot directly through WhatsApp for quick answers to common health questions.  (Explain how the chatbot is integrated and what it can do.  Mention any specific commands or functionalities.)

**Note** works only on test mobile number
* **Disease Prediction:**  Enter your symptoms to receive potential disease predictions based on a trained machine learning model. (Mention the accuracy or limitations of the model.  Explain what type of diseases are covered.)
* **Report Generation:** Generate comprehensive health reports based on user input and disease prediction results. (Describe the content of the report.)
* **First Aid Information:** Access a comprehensive database of first aid procedures for various common ailments. (Mention the source of the first aid information.)
* **Government Healthcare Policies:**  Stay informed about various government healthcare policies and programs. (Specify which regions or countries the policies cover.)

## Technologies Used

* **Streamlit:** For creating the interactive web application.
* **NumPy:** For numerical computing and data manipulation.
* **Pandas:** For data analysis and working with datasets.
* **Joblib:** For saving and loading machine learning models.
* **Scikit-learn:** For machine learning model training and evaluation.
* **Google Colab:** For development and model training.
* **Bot Press:** For user query and Knowledge base 
* **WhatsApp API Integration:** Bootstrapped with botpress.

## Installation

1. Clone the repository:
   bash
   git clone https://github.com/Shivang1611/SwasthyaGuide
   

2. Navigate to the project directory:
   ```bash
   cd SwasthyaGuide
   ```

3. Create a virtual environment (recommended):
   ```bash
   python3 -m venv venv  # Or python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt  # Create a requirements.txt file listing all dependencies
   ```
   


## Usage

1. Run the Streamlit app:
   ```bash
   python -m streamlit run pages/home.py  
   ```

2. Access the app in your web browser at [streamlit](https://swasthyaguide.streamlit.app/).

3. Follow the on-screen instructions to use the different features.




## Contributing

Contributions are welcome!  Please open an issue or submit a pull request if you'd like to contribute to the project.

