pipeline {
    agent any
    stages {
        stage('requirements') {
            steps {
                    bat 'pip install -r requirements.in'
            }
        }
        stage('data_creation') {
            steps {
                    bat "./pipeline.sh data_creation"
            }
        }
        stage('model_preprocessing') {
            steps {
                    bat "./pipeline.sh model_preprocessing.py"
            }
        }
        stage('model_preparation') {
            steps {
                    bat "./pipeline.sh model_preparation"
            }
        }
        stage('model_testing') {
            steps {
                    bat "./pipeline.sh model_testing"
            }
        }
    
    }
}