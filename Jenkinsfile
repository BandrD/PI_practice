pipeline {
    agent any
    stages {
        stage('requirements') {
            steps {
                dir('PI_practice'){
                    sh 'pip install -r requirements.in'
                }
            }
        }
        stage('data_creation') {
            steps {
                dir('PI_practice'){
                    sh 'python3 data_creation.py'
                }
            }
        }
        stage('model_preprocessing') {
            steps {
                dir('PI_practice'){
                    sh 'python3 model_preprocessing.py'
                }
            }
        }
        stage('model_preparation') {
            steps {
                dir('PI_practice'){
                    sh 'python3 model_preparation.py'
                }
            }
        }
        stage('model_testing') {
            steps {
                dir('PI_practice'){
                    sh 'python3 model_testing.py'
                }
            }
        }
    
    }
}