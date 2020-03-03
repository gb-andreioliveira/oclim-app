pipeline {
  agent any
  stages {
    stage('Assemble') {
      steps {
        echo 'Starting Assembly!'
      }
    }

    stage('Build App') {
      steps {
        build 'oclim-app'
      }
    }

  }
}