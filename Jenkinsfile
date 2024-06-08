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
         stage('preprocess_data') {
            steps {
                bat 'dvc repro preprocess'
            }
        }
        stage('train_model') {
            steps {
                bat 'dvc repro train'
            }
        }
        stage('evaluate_model') {
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