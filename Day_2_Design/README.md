
# Welcome to My 2nd Desing and Develop CDK Python project!

## Design 2 Problem Statement:
Consider that you are getting events in the format [{“event1”:{“attr1”: value }}] from  different APIs.  
1) How will you parse the event to get the value?  
2) How will you return 10 latest events when required? 

## Design 
Given below is the design for the above problem
![](https://user-images.githubusercontent.com/107042677/184424960-02f2efb9-7d3c-4768-9f66-32038a234e16.png)

## Environment Setup
* First install Windows Subsystem for Linux (WSL). For this, download WSL.exe file from Google. I faced error in installtion using wsl --install command so I used wsl.exe --install -d Ubuntu-20.04 commad to install it correctly.
* Dwnloaded VS Code and setup remote WSL from windows
* Download python3
* Donwload awscliv2.zip file from given path and install AWS. If you download it directly from google, there will be issue of path.
* Download and install NVM and NPM
* Check versions of all to be sure that softwares are installed corrrectly.

## Project Deployment - How to Run
* Open the ubuntu terminal and clone the git repository using git clone `forked-repo-github-url`
* Confirm that your working directory is Sprint5_day2
* Activate the virtual environment using command `source .venv/bin/activate`
* Configure the aws using aws configure and add your email and username to global configuration using command `git config --global user.email "your-email.gmail.com"` and `git config --global user.name "your-name"`
* Edit commands in pipelines_.ShellStep to add path of your directory. cd RootFolderName/ProjectFolderName/
* Run `pip install -r requirements.txt to install` all required packages
* Push changes to github. git commit -m "commit message" and git push
* Synth and Deploy the project on Consile using cdk synth and cdk deploy.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
