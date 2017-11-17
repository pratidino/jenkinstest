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
}
