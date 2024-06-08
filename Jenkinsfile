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
                    sh "./pipeline.sh data_creation"
                }
            }
        }
        stage('model_preprocessing') {
            steps {
                dir('PI_practice'){
                    sh "./pipeline.sh model_preprocessing.py"
                }
            }
        }
        stage('model_preparation') {
            steps {
                dir('PI_practice'){
                    sh "./pipeline.sh model_preparation"
                }
            }
        }
        stage('model_testing') {
            steps {
                dir('PI_practice'){
                    sh "./pipeline.sh model_testing"
                }
            }
        }
    
    }
}