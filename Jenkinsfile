pipeline {
    agent none
    stages {
        stage('Build') {
	    agent{docker{image 'python:3.5.1'}}
            steps {
                sh 'python --version'
            }
        }
        stage('Test 1') {
	    agent{docker{image 'python:3.5.1'}}
            steps {
                sh 'python --version'
                sh 'python test.py'
            }
        }
        stage('Test 2 - unittest'){
	    agent{
		docker{
			image 'qnib/pytest'
		}
	    }
            steps {
	    	  sh 'py.test --verbose --junit-xml test-reports/results.xml test_test.py'
            }
        }
	stage('Build Container'){
	    def image = docker.build("pytest1:${env.BUILD_ID}")
	}
	stage('Sanity check'){
	    steps{
		input "Does this Staging look OK to you?"
	    }
	}
        stage('Deploy - Production'){
	    def image = docker.build("pytest1:${env.BUILD_ID}")
	    image.push()
	    image.push('latest')
	}
    }
    post{
        always{
            echo 'End of pipeline'
        }
    }
}
