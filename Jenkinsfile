pipeline {
    agent any
    stages {
        stage('One') {
            steps {
                sh 'echo "Hi,this is Pratyusha"'
            }
        }
        stage('Two') {
            steps {
                input('Do you want to proceed?')
            }
        }
        stage('Three') {
            when {
                not {
                    branch "feature"
                }
            }
            steps {
                echo "When not condition succeeds this execuets"
            }
        }
        stage ('Four') {
            parallel {
                stage ('Four.One') {
                    steps {
                        echo "Running...."
                    }
                }
            }
        }
        stage ('Five') {
            steps {
                retry(2) {
                    echo "Retrying for 2 times.."
                }
                timeout(time:1, unit:'MINUTES') {
                    echo "Timeout"
                }
            }
        }
    }
            
            
                    
        
