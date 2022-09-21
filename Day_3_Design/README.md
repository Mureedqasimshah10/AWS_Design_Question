
# Welcome to My Day 3 Desing project!

Create a design for the following application: 
The Australian property market has undergone “unprecedented growth” in the past two years due to  the low-interest rates and strong consumer confidence (Thomas, 2022). This results in significant  movements and transactions within the property market that will increase the digital traffic to real  websites as more people sell, buy or rent properties. Design an application that allows the property  owner and purchaser/tenant to match based on factors detailed below. Property owner will upload their  properties for sale or rent on the application. They should also be able to input their desired  characteristics of buyers and tenants as criteria (e.g. family size, nationality etc). Purchaser or tenant  will then be able to browse for the property based on price, location, proximity to school and transport station. 

## Design 
Given below is the design for the above problem
![](https://user-images.githubusercontent.com/107042677/184476391-5154e86f-9882-49f7-8921-c8edec2e7ae5.jpg)

## Explanation
So here in the above diagram we have to user. One is admin (seller) and the other one is buyer. After that we have an API Gateway which is further connected with lambda function. So API will make a request by invoking the lambda function. If someone want to buy then he will use GET method to retrive the data from the dynamodb table and if somneone want to sell then he may want to store the property pictures or videos, so he will store these things in the S3 and a link can be send into the dynamodb table. 
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
