pipeline {
    agent any

    environment {
        PYTHON_ENV = '/usr/bin/python3'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run FastAPI Application') {
            steps {
                script {
                    sh 'uvicorn main:app --reload &'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'pytest test_prime.py'
                }
            }
        }

        stage('Report to GitHub') {
            steps {
                script {
                    currentBuild.result = 'SUCCESS'
                }
            }
        }
    }

    post {
        success {
            echo 'Build and tests were successful!'
        }
        failure {
            echo 'Build or tests failed.'
        }
        always {
            cleanWs()
        }
    }
}

