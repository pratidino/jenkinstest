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
                sh 'python -c 1000000 + 1000000'
            }
        }
        stage('Deploy - Staging'){
            steps {
                echo 'Deploying in staging'
                echo 'copy to Staging env'
                echo 'Running.. smoke test'
            }
        }
        stage('Deploy - Production'){
            steps{
                echo 'Deploying in Production'
                echo 'copy to Prod'
                echo 'restarting services'
            }
        }
    }
    post{
        always{
            echo 'End of pipeline'
        }
    }
}
