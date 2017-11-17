pipeline {
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
