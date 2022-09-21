
# Design & Develop Day 7 Project
---

### Design Problem Statement:
---
Suppose there are 10 files uploading to S3 bucket each day. For each file received
on cloud storage, you have a mechanism to process the file. During the processing, your code parses
the text and counts the number of times each word is repeated in the file. For example, in the following text: “Hello World and Hello There”, your code should be able to say that "hello" has been used twice, "world" has occured once and so on. Then it will store the results in some storage and email to some email address after successful processing.

## Proposed Design
---
![](https://user-images.githubusercontent.com/107042677/185043424-937ae1f7-db70-4621-8555-7af7b2f5968c.png)
## Environment Setup
* First install Windows Subsystem for Linux (WSL). For this, download WSL.exe file from Google. I faced error in installtion using wsl --install command so I used wsl.exe --install -d Ubuntu-20.04 commad to install it correctly.
* Dwnloaded VS Code and setup remote WSL from windows
* Download python3
* Donwload awscliv2.zip file from given path and install AWS. If you download it directly from google, there will be issue of path.
* Download and install NVM and NPM Check versions of all to be sure that softwares are installed corrrectly.

## Project Deployment - How to Run
---

* Open the ubuntu terminal and clone the git repository using git clone forked-repo-github-url Confirm that your working directory is `Sprint5_day7`
* Activate the virtual environment using command source .venv/bin/activate Configure the aws using aws configure and add your email and username to global configuration using command `git config --global user.email "your-email.gmail.com"` and `git config --global user.name "your-name"`
* Edit commands in pipelines_.ShellStep to add path of your directory. cd RootFolderName/ProjectFolderName/
* Run `pip install -r requirements.txt` to install all required packages
* Push changes to github. git commit -m "commit message" and git push Synth and Deploy the project on Consile using cdk synth and cdk deploy.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
