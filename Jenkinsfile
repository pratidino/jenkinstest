pipeline {
    agent { 
        docker 'python:3.5.1'
    }
    stages {
        stage('Build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Test') {
            steps {
                sh 'python --version'
                sh 'python test.py'
            }
        }
    }
}
