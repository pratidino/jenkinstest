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
        stage('Test'){        
            agent { docker 'python:3.5.1' }
            steps {
            python test.py
            }
        }
    }
}
