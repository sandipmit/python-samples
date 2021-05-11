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
              
                sh '''
                $CONDA_PATH/conda env create -f environment.yml -n $CONDA_ENV  || $CONDA_PATH/conda env update -f environment.yml -n $CONDA_ENV --prune
                echo 'user name is - ' 
                whoami
                '''
            }
        }
        stage('Unit Testing') {
            steps {
                echo 'Unit testing..'
                sh '''
                echo $PATH
                echo $HOME
                
                echo "My current shell is $SHELL ($0)"
                    
                source /opt/anaconda3/etc/profile.d/conda.sh
                conda init bash   
                source ~/.bashrc
                conda activate $CONDA_ENV
                echo '***************List of packages****************'
                conda list
                pytest --cov=unit_testcases --cov-report html:cov_html   unit_testcases --html=report.html --self-contained-html
                
                #$CONDA_PATH/pytest --cov=unit_testcases --cov-report html:cov_html   unit_testcases --html=report.html --self-contained-html
                '''
                
               
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
      post {  
         always {  
             echo 'This will always run'  
             mail bcc: '', body: "<b>Example</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR CI: Project name -> ${env.JOB_NAME}", to: "sdhummad@cppib.com";               
         }  
         success {  
             echo 'This will run only if successful'  
         }  
         failure { 
             echo 'Pipeline failed' 
             mail bcc: '', body: "<b>Example</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR CI: Project name -> ${env.JOB_NAME}", to: "sdhummad@cppib.com";  
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
