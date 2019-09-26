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
	    steps{
	        sh 'sudo docker build -t pytest1 .'
		sh 'sudo docker push gpratidi/pytest1:latest'
	    }
	}
        stage('Deploy - Staging'){
	    agent{
	        docker{
		    image 'gpratidi/pytest1:latest'
		}
	    }
            steps {
                echo 'Deploying in staging'
                echo 'Running it..'
                sh '/home/app/test.py'
            }
        }
	stage('Sanity check'){
	    steps{
		input "Does this Staging look OK to you?"
	    }
	}
        stage('Deploy - Production'){
	    agent{
	        docker{
		   image 'gpratidi/pytest1:latest'
		}
	    }
            steps{
                echo 'Deploying in Production'
                echo 'Running in Production..'
                sh '/home/app/test.py'
            }
        }
    }
    post{
        always{
            echo 'End of pipeline'
        }
    }
}
