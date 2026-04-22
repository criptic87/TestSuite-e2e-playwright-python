pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python3 --version'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                sh 'playwright install chromium --with-deps'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/ -v'
            }
        }
    }

    post {
        always {
            junit 'test-results/*.xml'    // publish test results
        }
        failure {
            echo 'Tests failed — notify team'
        }
        success {
            echo 'All tests passed'
        }
    }
}