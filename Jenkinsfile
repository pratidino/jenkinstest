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
		input "Does this look OK to you?"
	    }
	}
        stage('Push container'){
            agent any
            steps{
		    echo 'Push docker image'
		    sh 'docker tag pytest1 gpratidi/pytest1:$BUILD_NUMBER'
		    
		    sh 'docker push gpratidi/pytest1:$BUILD_NUMBER'
		    sh 'docker push gpratidi/pytest1:latest'
	    }
	}
	stage('Test Container'){
	    agent{
	        docker{
		    image 'gpratidi/pytest1'
		}
	    }
	    steps{
	        sh 'python --version'
		sh 'python test.py'
	    }
	}
	stage('Deploy in production'){
	   agent any
	   steps{
	       sh 'deploying in Prod'
	   }
	}
    }
}