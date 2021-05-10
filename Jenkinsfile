pipeline {
    agent any
    
    environment {
        CONDA_PATH = '/opt/anaconda3/bin'
        CONDA_ENV = 'test'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building Conda ENV....'
                echo "Conda ENV name is ${CONDA_ENV}"

                sh '''#!/usr/bin/env bash
                $CONDA_PATH/conda env create -f environment.yml -n $CONDA_ENV  || $CONDA_PATH/conda env update -f environment.yml -n $CONDA_ENV --prune
                
                $CONDA_PATH/conda init bash
                source /var/lib/jenkins/.bashrc
                '''
            }
        }
        stage('Unit Testing') {
            steps {
                echo 'Unit testing..'
                sh '''#!/usr/bin/env bash
                echo $PATH
                echo $HOME
                $CONDA_PATH/conda activate $CONDA_ENV
                # update git
                #~/git/update.sh
                #cd $WORKSPACE
                python -m pytest -n auto --html=report.html --cov-report html --cov-report annotate --cov=unit tests unit_testcases --junitxml=pytest-report.xml --cov-report xml --cov-report term --cov-branch
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
