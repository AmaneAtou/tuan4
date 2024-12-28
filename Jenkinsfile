pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'python -m pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'python -m pytest test_main.py -v'
            }
        }
        
        stage('Run Application') {
            steps {
                sh 'python -m uvicorn main:app --reload'
            }
        }
    }
    
    post {
        always {
            githubCheck(
                name: 'Jenkins Build',
                conclusion: currentBuild.currentResult,
                detailsURL: env.BUILD_URL
            )
        }
    }
}
