#!groovy
@Library("jenkins-shared-lib") _
ciPythonBuild {
    appGit = "https://github.com/gb-andreioliveira/oclim-app.git"
    appName = "app_oclim"
    s3Bucket = "oclim-terraform-s3"
    stackGit = "https://github.com/gb-andreioliveira/terraform-deploy"
    vpcName = "oclim-terraform"
    subnet1 = "oclim-terraform-publicsubnet-1"
    subnet2 = "oclim-terraform-publicsubnet-2"
    internal_security_group = "oclim-terraform-InternalSG"
    external_security_group = "oclim-terraform-externalSG"

}