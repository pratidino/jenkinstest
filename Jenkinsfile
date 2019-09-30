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
	    environment{
	        registry = "gpratidi/pytest1"
		registryCredential = 'docker-hub-creds'
	    }
 	    agent any
	    steps{
	        script{
		    docker.build registry + ":$BUILD_NUMBER"
		}
	    }
	}
	stage('Sanity check'){
	    steps{
		input "Does this Staging look OK to you?"
	    }
	}
        stage('Deploy - Production'){
            environment{
	        registry = "gpratidi/pytest1"
		registryCredential = 'docker-hub-creds'
	    }
	    
            agent any
            steps{
	        script{
		    docker.push()
		    docker.push('latest')
		}
	    }
	}
    }
    post{
        always{
            echo 'End of pipeline'
        }
    }
}
