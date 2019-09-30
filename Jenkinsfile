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
	    agent any
	    steps{
		   echo 'Docker build'
		   sh 'docker build -t pytest1 /home/nino/jenkinstest/'
	    }
	}
	stage('Sanity check'){
	    agent any
	    steps{
	        echo 'Test Docker image'
		sh 'docker run -it pytest1 python /app/test.py'
		input "Does this look OK to you?"
	    }
	}
        stage('Deploy - Production'){
            environment{
	        registry = "gpratidi/pytest1"
		registryCredential = 'docker-hub-creds'
	    }
	    
            agent any
            steps{
		    echo 'Push docker image'
		    sh 'docker tag pytest1 registry:$BUILD_NUMBER'
		    sh 'docker push registry:$BUILD_NUMBER'
		    sh 'docker push registry:latest'
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
