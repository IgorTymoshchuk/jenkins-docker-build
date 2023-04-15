pipeline {
	agent{
		label 'linux'
	}

	environment {
		DOCKER_IMAGE_NAME = "ontirex/jenkins-build"
		DOCKER_IMAGE_TAG = "latest"
		
		aws_access_key_id = ""
		aws_secret_access_key = ""
		aws_region = "eu-central-1"
		ec2_instance_state_code = "80"
	}

	stages {
		stage('Initialize') {
			steps {
				cleanWs()
			}
		}
		
		stage('Checkout') {
			steps {
				checkout([$class: 'GitSCM',
				branches: [[name: 'main']],
				doGenerateSubmoduleConfigurations: false,
				extensions: [],
				submoduleCfg: [],
				userRemoteConfigs: [[url: 'https://github.com/IgorTymoshchuk/jenkins-docker-build.git']]])
			}
		}
		
		stage('Print Working Directory Content'){
			
			steps{
				sh 'ls -la'
			}
		}
		
		
		stage('Build Docker image') {
			steps{
			    script {
				    dockerImage = docker.build("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}")
			    }
		    }
		}
		
		stage('Push Docker image') {
			steps{
			    script {
    				withDockerRegistry([ credentialsId: "DOCKER_HUB_CREDENTIALS", url: "" ]) {
    					dockerImage.push()
    				}
			    }
			}
		}
	}
	post {
		success {
			// Send a notification on success
			sh 'echo "Docker image build succeeded!"'
		}
		failure {
			// Send a notification on failure
			sh 'echo "Docker image build failed!"'
		}
	}
}
