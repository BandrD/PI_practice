pipeline {
    agent any
    stages {
        stage('Clone repository') {
            steps {
                git 'https://https://github.com/BandrD/PI_practice.git'
            }
        }
        stage('Setup environment') {
            steps {
                sh 'pip install -r requirements.in'
            }
        }
        stage('Run tests') {
            steps {
                sh 'pytest test_predict'
            }
        }
        stage('Build Docker image') {
            steps {
                sh 'docker build -t BandrD/PI_practice .'
            }
        }
        stage('Push Docker image') {
            steps {
                withDockerRegistry([ credentialsId: 'docker-hub-credentials', url: '' ]) {
                    sh 'docker push BandrD/PI_practice'
                }
            }
        }
    }
}