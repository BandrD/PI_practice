pipeline {
    agent any
    stages {
        stage('requirements') {
            steps {
                    sh 'pip install -r requirements.in'
            }
        }
        stage('data_creation') {
            steps {
                    sh "./pipeline.sh data_creation"
            }
        }
        stage('model_preprocessing') {
            steps {
                    sh "./pipeline.sh model_preprocessing.py"
            }
        }
        stage('model_preparation') {
            steps {
                    sh "./pipeline.sh model_preparation"
            }
        }
        stage('model_testing') {
            steps {
                    sh "./pipeline.sh model_testing"
            }
        }
    
    }
}