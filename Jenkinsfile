pipeline {
    agent any

    environment {
        VIRTUAL_ENV = 'myenv' // Tên thư mục môi trường ảo
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Tải mã nguồn từ GitHub
                git 'https://github.com/AmaneAtou/tuan4.git'  // Thay URL với repo của bạn
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                script {
                    // Tạo môi trường ảo và cài đặt dependencies
                    sh 'python3 -m venv $VIRTUAL_ENV'
                    sh '$VIRTUAL_ENV/bin/pip install -r requirements.txt'  // Cài đặt các thư viện từ requirements.txt
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
                    // Chạy pytest để kiểm tra ứng dụng
                    sh '$VIRTUAL_ENV/bin/pytest test_main.py'
                }
            }
        }

        stage('Publish Test Results') {
            steps {
                // Xuất kết quả kiểm tra dưới dạng JUnit
                junit '**/test-*.xml'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // Dọn dẹp tài nguyên sau khi pipeline hoàn thành
        }
    }
}

