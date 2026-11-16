
pipeline {
    agent any

    stages {
        stage('Preparation') {
            steps {
                echo 'Preparation du projet...'
            }
        }

        stage('Build') {
            steps {
                echo 'Construction du projet...'
            }
        }

        stage('Test') {
            steps {
                echo 'Execution des tests...'
            }
        }
    }

    post {
        success {
            echo 'Pipeline execute avec succes !'
        }
        failure {
            echo 'Le pipeline a echoue.'
        }
    }
}
