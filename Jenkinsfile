
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out Grade System Version 1'
            }
        }

        stage('Check Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }
    }

    post {
        success {
            echo 'Grade System V1 pipeline completed successfully!'
        }
        failure {
            echo 'Grade System V1 pipeline failed. Check the console output.'
        }
    }
}
