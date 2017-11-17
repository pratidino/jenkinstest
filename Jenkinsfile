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
    }
    agent { 
        docker { image 'python: 3.5.1'}
    }
    stages {
        stage('Test') {
            steps {
                sh 'python --version'
                sh 'python test.py'
            }
        }
    }
}
