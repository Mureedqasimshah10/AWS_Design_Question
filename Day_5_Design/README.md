
# Design & Develop Day 5 Project
---

## Design Problem Statement:
---
How would you automate deployment (e-g on AWS) for a system that has:  
a) Source code in a repo  
b) How do we generate an artifact from the repo that gets published and later is used in some services?  
c) Are there more than one solutions? 

## Proposed Design
---
Given below is the proposed design for the above problem.
![](https://user-images.githubusercontent.com/107042677/184634785-508892b1-8cde-4d65-b288-42c1aadaf5f2.png)

### Question1
## How would you automate deployment?
---
The deployment can be made automate by using cicd pipeline connected to a source control services like Git.
Further it has three stages shown in the design.
1) Source stage: When commit is made, it triggers the CICD Pipeline.
2) Build/Test Stage: Codebuild which will build and synthesize the code. Runs the test like unit test, functionla test and integration test. If the tests are successfull then deploy stage is triggered.

### Question 2
## How do we generate an artifact from the repo that gets published and later is used in some services? 
---
We can generate an artifact from the repo using our codebuild within the pipeline. this artifict will be stored in the s3 bucket. we can share the urls for thoes artifacts that can be used by the services as well. 

### Question 3
## Are there more than one solutions? 
---
Yes I think more than one solution is possible. You can use any other aws resources or 3rd party services as well.


## Environment Setup
---
* First install Windows Subsystem for Linux (WSL). For this, download WSL.exe file from Google. I faced error in installtion using wsl --install command so I used wsl.exe --install -d Ubuntu-20.04 commad to install it correctly.
* Dwnloaded VS Code and setup remote WSL from windows
* Download python3
* Donwload awscliv2.zip file from given path and install AWS. If you download it directly from google, there will be issue of path.
Download and install NVM and NPM Check versions of all to be sure that softwares are installed corrrectly.

## Project Deployment - How to Run
---
* Open the ubuntu terminal and clone the git repository using git clone forked-repo-github-url
* Confirm that your working directory is `Sprint5_day5`
* Activate the virtual environment using command `source .venv/bin/activate`
Configure the aws using aws configure and add your email and username to global configuration using command `git config --global user.email "your-email.gmail.com"` and `git config --global user.name "your-name"`
* Edit commands in pipelines_.ShellStep to add path of your directory. cd RootFolderName/ProjectFolderName/
* Run pip install -r requirements.txt to install all required packages
* Push changes to github. git commit -m "commit message" and git push Synth and Deploy the project on * Consile using cdk synth and cdk deploy.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
