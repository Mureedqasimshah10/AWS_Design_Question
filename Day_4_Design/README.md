
# Design & Develop Day 4 Project
---
## Design Problem Statement:
---
Deploy, maintain and rollback pipeline for an artifact deployment e-g lambda  package, docker image etc.
1) What do you think if the latest deployment is failing? 
2) How will you rollback?  
3) How do you reduce such failures so there is less need to rollback

## Proposed Design
---
Given below is the proposed design for the above problem.
![](https://user-images.githubusercontent.com/107042677/184634785-508892b1-8cde-4d65-b288-42c1aadaf5f2.png)

### Question 1:
What do you think if the latest deployment is failing?  
---
There could be many reason for the latest deployment failing.
* Not explicitly defining the polices will lead towards the latest deployment failing.
* Codepipeline not having access to the repository
* Deployment can fails due to the different regions as well.
### Question 2:
How will you rollback?    
---
* 1: We can rollback by defining lambda deployment group. Its configuration will be used by Codedeploy during deployment.
* 2: Another way we can rollback by defining the alarms. If an alarm reached the specified thrashold then it will rollback. It should also define in deployment groups as well.
### Question 3:
How do you reduce such failures so there is less need to rollback?
---
* We can reduce such kind of failures by creating the different test like Unit test,  functional test and intergration test. 
## Environment Setup
---
* First install Windows Subsystem for Linux (WSL). For this, download WSL.exe file from Google. I faced error in installtion using wsl --install command so I used wsl.exe --install -d Ubuntu-20.04 commad to install it correctly.
* Dwnloaded VS Code and setup remote WSL from windows
* Download python3
* Donwload awscliv2.zip file from given path and install AWS. If you download it directly from google, there will be issue of path.
* Download and install NVM and NPM
Check versions of all to be sure that softwares are installed corrrectly.

## Project Deployment - How to Run
___
* Open the ubuntu terminal and clone the git repository using git clone forked-repo-github-url
* Confirm that your working directory is Sprint5_day4
* Activate the virtual environment using command source .venv/bin/activate
* Configure the aws using aws configure and add your email and username to global configuration using command git config --global user.email "your-email.gmail.com" and git config --global user.name "your-name"
* Edit commands in pipelines_.ShellStep to add path of your directory. cd RootFolderName/ProjectFolderName/
* Run pip install -r requirements.txt to install all required packages
* Push changes to github. git commit -m "commit message" and git push
Synth and Deploy the project on Consile using cdk synth and cdk deploy.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
