pipeline {
    agent any

    environment {
        VIRTUAL_ENV = 'myenv' 
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Tải mã nguồn từ GitHub
                git 'https://github.com/AmaneAtou/tuan4.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                script {
                    // Tạo môi trường ảo và cài đặt dependencies
                    sh 'python3 -m venv $VIRTUAL_ENV'
                    sh '$VIRTUAL_ENV/bin/pip install --upgrade pip'
                    sh '$VIRTUAL_ENV/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run FastAPI') {
            steps {
                script {
                    // Chạy FastAPI ứng dụng trong nền
                    sh '$VIRTUAL_ENV/bin/uvicorn main:app --host 0.0.0.0 --port 8000 &'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Chạy pytest để kiểm tra ứng dụng và tạo báo cáo XML
                    sh '$VIRTUAL_ENV/bin/pytest --junitxml=test-results.xml test_prime.py'
                }
            }
        }

        stage('Publish Test Results') {
            steps {
                junit 'test-results.xml'  // Đăng kết quả kiểm tra lên Jenkins
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            script {
                // Kiểm tra và dừng FastAPI nếu đang chạy
                def pid = sh(script: "lsof -t -i:8000 || true", returnStdout: true).trim()
                if (pid) {
                    echo "Killing process with PID: ${pid}"
                    sh "kill ${pid}"
                } else {
                    echo "No process running on port 8000"
                }
            }

            // Gửi kết quả kiểm tra lên GitHub Checks
            script {
                def status = currentBuild.currentResult
                def conclusion = status == 'SUCCESS' ? 'SUCCESS' : 'FAILURE'  // Dùng giá trị hợp lệ là 'SUCCESS' hoặc 'FAILURE'
                
                publishChecks(
                    name: 'Test Results',
                    conclusion: conclusion  // Loại bỏ tham số description
                )
            }
        }
    }
}

