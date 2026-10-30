pipeline {
    agent any

    environment {
        PYTHON = 'C:/Users/91702/AppData/Local/Programs/Python/Python312-32/python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out Grade System Version 1'
            }
        }

        stage('Check Python') {
            steps {
                bat '"%PYTHON%" --version'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat '"%PYTHON%" -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\python.exe -m pytest -v'
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

