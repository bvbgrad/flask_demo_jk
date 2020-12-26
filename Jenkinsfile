pipeline {
    agent any
    stages {
        stage('Build') {
            agent {
                docker { image 'node:14-alpine' }
            }
            steps {
                sh 'node --version'
                echo "build stage"
            }
        }
        stage('Test') {
            steps {
                echo "Successful test!"
            }
        }
        stage('Depoly') {
            steps {
                echo "Failed deploy!"
            }
        }
    }
    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}
