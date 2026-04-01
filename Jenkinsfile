pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                sh '''
                  python3 -m venv venv
                  . venv/bin/activate
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                  . venv/bin/activate
                  python - <<EOF
print("Test stage passed")
EOF
                '''
            }
        }

        stage('Run') {
            steps {
                sh '''
                  . venv/bin/activate
                  python hello.py
                '''
            }
        }
    }
}
