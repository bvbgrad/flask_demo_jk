pipeline {
    agent {
        docker { image 'node:14-alpine' }
    }
    stages {
        stage('Build') {
            steps {
                sh 'echo "Build success!"';
                sh  'node --version';
                exit 0'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Successful test!"; exit 0'
            }
        }
        stage('Depoly') {
            steps {
                sh 'echo "Failed deploy!"; exit 1'
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
