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
        stage('run_data_test') {
            steps {
                    bat "./pipeline.sh test_predict"
            }
        }
        stage('run_model_test') {
            steps {
                    bat "./pipeline.sh model_test"
            }
        }
    }
}