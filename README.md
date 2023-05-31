<h1>Diabetes Predictor</h1>

The Diabetes Predictor is a web application built using a powerful Python web framework Django and integrated with a machine learning model. This project aims to provide accurate predictions about the likelihood of an individual developing diabetes based on various input parameters.

The repository includes the complete source code, including the trained machine learning model located in the "MLmodel" directory. This project has been deployed on an AWS EC2 instance, the address is http://3.76.43.69:8000/ 

<h2>Features</h2>

Prediction Model: The application is equipped with a trained machine learning model that takes input data related to various health parameters (e.g., glucose level, BMI, heart disease) and provides a prediction of the likelihood of diabetes.

User Interface: The web application offers a user-friendly interface where users can input their health parameters and obtain a prediction instantly.

<h2>Instructions</h2>

To run the Diabetes Predictor project locally, follow these steps:

Clone the repository: 'git clone https://github.com/farzanasumona/diabetes-predictor-machine-learning-project.git'

Install project dependencies: pip install -r requirements.txt

Start the development server: python manage.py runserver

Access the application in browser at http://localhost:8000

<h2>Dataset</h2>

The machine learning model used in this project was trained on a well-curated dataset containing information related to diabetes diagnosis. The dataset included in this repository as a CSV file located in the directory named "MLmodel". 
