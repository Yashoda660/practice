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
                  set -e
                  python3 -m venv venv
                  . venv/bin/activate
                  python -m pip install --upgrade pip
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                  set -e
                  . venv/bin/activate
                  python - <<'EOF'
print("Test stage passed")
EOF
                '''
            }
        }

        stage('Run hello.py') {
            when {
                expression { return fileExists('hello.py') }
            }
            steps {
                sh '''
                  set -e
                  . venv/bin/activate
                  python hello.py | tee hello_output.txt
                '''
            }
        }

        stage('Run python.py') {
            when {
                expression { return fileExists('python.py') }
            }
            steps {
                sh '''
                  set -e
                  . venv/bin/activate
                  python python.py | tee python_output.txt
                '''
            }
        }
    }

    post {
        always {
            // Archive any outputs if they exist
            script {
                if (fileExists('hello_output.txt') || fileExists('python_output.txt')) {
                    archiveArtifacts artifacts: '*.txt', fingerprint: true
                }
            }
            cleanWs()
        }
    }
}
