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
        stage('Test 1') {
            steps {
                sh 'python --version'
                sh 'python test.py'
            }
        }
        stage('Test 2'){
            steps {
                sh 'python 1000000 + 1000000'
            }
        }
    }
}
