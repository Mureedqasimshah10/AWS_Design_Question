# Design & Develop Day 8 Project
---

### Design Problem Statement:
---

Create a design for the following application:
As everyone has been experiencing, there has been an increase in the price of goods and services
whether it is because of unstable environmental factors or the state of the current economy. Design an
application that will collect and analyze users’ expenditure data (images of receipts taken from the
mobile camera, manually adding expense information ) to present users their personal consumption
structure, to manage their everyday finances so that users can deal with their budget and expenses to
save money. The application should be able to recognize words and prices from receipts, sort itemsinto specific categories, analyse and calculate the amount of each category at the end of a particular period. The application should also:
* (a) Remind users of excessed budget and provides expenditure summary
* (b) Create a projection of monthly expenses that the users have
* (c) Provide a goal for users so that they are motivated to manage their daily finances well

## Proposed Design
---
![](https://user-images.githubusercontent.com/107042677/185334739-0de2cac6-2f84-48e7-94ad-10c79687a102.jpg)

## Environment Setup
---

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
