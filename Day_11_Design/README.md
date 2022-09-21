
# Design & Develop Day 11 Project
---

### Design Problem Statement:
---
What if we have 15MB file that we have to upload on S3 using API gateway. We have the limitation that our API gateway has the maximum payload capacity of 10MB. How you will
solve this problem?

## Proposed Design First Approach using WebSocket API & Enabling compression
---

![](https://user-images.githubusercontent.com/107042677/185783289-db007dd6-8062-4ce4-88ae-abbd13f92898.png)

## Proposed Design Second Approach using presigned URLs
---
![](https://user-images.githubusercontent.com/107042677/185783331-3ff8722c-68ff-4fe3-8b8c-2d29c8425812.png)

## Environment Setup
---

* First install Windows Subsystem for Linux (WSL). For this, download WSL.exe file from Google. I faced error in installtion using wsl --install command so I used wsl.exe --install -d Ubuntu-20.04 commad to install it correctly.
* Dwnloaded VS Code and setup remote WSL from windows
* Download python3
* Donwload awscliv2.zip file from given path and install AWS. If you download it directly from google, there will be issue of path.
* Download and install NVM and NPM Check versions of all to be sure that softwares are installed corrrectly.

## Project Deployment - How to Run
---

* Open the ubuntu terminal and clone the git repository using git clone forked-repo-github-url Confirm that your working directory is `Sprint5_day11`
* Activate the virtual environment using command source .venv/bin/activate Configure the aws using aws configure and add your email and username to global configuration using command `git config --global user.email "your-email.gmail.com"` and `git config --global user.name "your-name"`
* Edit commands in pipelines_.ShellStep to add path of your directory. cd RootFolderName/ProjectFolderName/
* Run `pip install -r requirements.txt` to install all required packages
* Push changes to github. git commit -m "commit message" and git push Synth and Deploy the project on Consile using cdk synth and cdk deploy.

## Useful Links

* https://dev.to/aws-builders/synchronous-aws-lambda-amazon-api-gateway-limits-and-what-to-do-about-them-2oec

* https://dev.to/aws-builders/processing-large-payloads-with-amazon-api-gateway-asynchronously-1m4f


## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
