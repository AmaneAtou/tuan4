pipeline {
    agent any

    environment {
        VIRTUAL_ENV = 'myenv' 
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/AmaneAtou/tuan4.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                script {
                    sh 'python3 -m venv $VIRTUAL_ENV'
                    sh '$VIRTUAL_ENV/bin/pip install --upgrade pip'
                    sh '$VIRTUAL_ENV/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run FastAPI') {
            steps {
                script {
                    sh '$VIRTUAL_ENV/bin/uvicorn main:app --host 0.0.0.0 --port 8000 &'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh '$VIRTUAL_ENV/bin/pytest --junitxml=test-results.xml test_prime.py'
                }
            }
        }

        stage('Publish Test Results') {
            steps {
                junit 'test-results.xml'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            script {
                def pid = sh(script: "lsof -t -i:8000 || true", returnStdout: true).trim()
                if (pid) {
                    echo "Killing process with PID: ${pid}"
                    sh "kill ${pid}"
                } else {
                    echo "No process running on port 8000"
                }
            }

            script {
                def status = currentBuild.currentResult
                def description = status == 'SUCCESS' ? 'Tests Passed' : 'Tests Failed'
                def conclusion = status == 'SUCCESS' ? 'success' : 'failure'
                
                githubChecks(
                    name: 'Test Results',
                    conclusion: conclusion,
                    description: description
                )
            }
        }
    }
}

