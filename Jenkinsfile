pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out..'
                //checkout scm
            }
        }
        stage('Unit Testing') {
            steps {
                echo 'Unit testing..'
                sh '''echo $PATH
                echo $HOME
                #set
                #export CONDA_PYTHON_EXE=$CONDA_PREFIX/envs/$CONDA_ENV/bin/python
                # export PATH=$CONDA_PREFIX/envs/$CONDA_ENV/bin:$PATH
                echo $PATH
                #PYTHONPATH=$WORKSPACE/src:$PYTHONPATH
                #source activate babylon
                # update git
                #~/git/update.sh
                #cd $WORKSPACE
                #python -m pytest -n auto --html=report.html --cov-report html --cov-report annotate --cov=babylon tests regression_tests --junitxml=pytest-report.xml --cov-report xml --cov-report term --cov-branch
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }

    environment {
        BB_HOME = '/home/ec2-user/git/babylon'
        CONDA_ENV = 'babylon'
        CMF_DATA_ACCESS_GIT = '/home/ec2-user/git/cmf-data-access/src'
  }
}