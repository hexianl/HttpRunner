pipeline {
  agent any
  stages {
    stage('master') {
      parallel {
        stage('master') {
          steps {
            sleep 5
          }
        }

        stage('dev') {
          steps {
            sleep 5
          }
        }

      }
    }

  }
}