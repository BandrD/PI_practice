pipeline {
    agent any
    stages {
        stage('requirements') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.in'
            }
        }
        stage('dvc_data_get') {
            steps {
                bat "dvc pull"
            }
        }
         stage('Preprocess data') {
            steps {
                bat 'dvc repro preprocess'
            }
        }
        stage('Train model') {
            steps {
                bat 'dvc repro train'
            }
        }
        stage('Evaluate model') {
            steps {
                bat 'dvc repro evaluate'
            }
        }
        stage('run_data_test') {
            steps {
                bat "pytest test_predict"
            }
        }
    }
}