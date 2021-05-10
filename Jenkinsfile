pipeline {
    agent any
    
    environment {
        CONDA_ENV = 'test'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building Conda ENV....'
                echo "Conda ENV name is ${CONDA_ENV}"

                sh '''#!/usr/bin/env bash
                #wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -nv -O miniconda.sh
                #bash miniconda.sh -b -p $WORKSPACE/miniconda
                #conda config --set always_yes yes --set changeps1 no
                #conda update -q conda
                /opt/anaconda3/bin/conda env create -f environment.yml -n $CONDA_ENV  || conda env update -f environment.yml -n $CONDA_ENV --prune
                '''
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
}
