node('master') {

  env.PATH = "${env.JENKINS_HOME}/bin:${env.PATH}"
  checkout scm

  stage('Get Ansible Roles') {
    dir('ansible/roles'){
      deleteDir()
    }
    dir('build') {
      deleteDir()
    }
    dir('dist') {
      deleteDir()
    }
    sh('#!/bin/sh -e\n' + 'ansible-galaxy install -r ansible/requirements.yml -p ansible/roles/ -f')
  }
  stage('Build ga-campaign-donations') {
    sh('#!/bin/sh -e\n' + "ansible-playbook -i 'localhost,' -c local --vault-password-file=${env.DEPLOY_KEY} ansible/playbook.yml --extra-vars 'target_hosts=all deploy_env=${env.DEPLOY_ENV} package_revision=${env.BUILD_NUMBER} gather_facts=yes' -t build -vvvv")
  }
  stage('Setup ga-campaign-donations') {
    sshagent (credentials: ['prov_1_key']) {
      withEnv(['ANSIBLE_REMOTE_TEMP=/tmp']) {
        sh('#!/bin/sh -e\n' + "ansible-playbook -i ansible/roles/inventory/${env.DEPLOY_ENV.toLowerCase()}/hosts --vault-password-file=${env.DEPLOY_KEY} --user=prov ansible/playbook.yml --extra-vars 'target_hosts=${env.DEPLOY_HOST} deploy_env=${env.DEPLOY_ENV} package_revision=${env.BUILD_NUMBER} workspace=${env.WORKSPACE}' -b -t deploy")
      }
    }
  }
  stage('Archive the ga-campaign-donations Packages') {
    dir('dist') {
      archiveArtifacts artifacts: '*.rpm'
      archiveArtifacts artifacts: '*.deb'
    }
  }
}