pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello"'
                sh '''
                   echo "Multiline also works"
                   ls -lah
                   '''
            }
        }
        agent { docker 'python:3.5.1' }
        stage('Test'){
            steps {
            python test.py
            }
        }
    }
}
