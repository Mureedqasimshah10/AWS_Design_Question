
# Design & Develop Day 10 Project
---

### Design Problem Statement:
---
A customer sends a request to an API Gateway endpoint. He wants a PDF report
to be generated in return. The problem is the max response time of API Gateway is 30 seconds. The
API Gateway is configured with a Lambda function that is responsible for performing the process of
generating PDF reports. Imagine, the customer wants a report of a huge chunk of data and the
processing time that the lambda will take can exceed 5 mins. The API Gateway can crash if its
processing/response time exceeds 30 secs. How would you tackle such a problem? The API Gateway
processing time is less than what the lambda function will take to perform the pdf generation process.
How we can manage to generate PDF report without making the API Gateway crash. How would you
tackle such a problem? Also, implement this application.

## Proposed Design First Approach using WebSocket API
---

![](https://user-images.githubusercontent.com/107042677/185735943-5b1ad11d-a78c-4138-93b9-4bb3e18746c9.png)

### How it's working:
---
Using the websocket api we can also avoid the API Gateway Invocation error issues since the API Gateway has 10 minutes ideal timeout limit and 2 hours communication duration which is more than enough for a 15 minutes duration the lambda function will run. So once the data can be collected from the website then the lambda function will generate the pdf file of that data and store it in the S3 bucket and the file link then be shared with user via same api gate way.

### Working of WebSocket API:
---

After the initial handshake between client and server, it allows for two-way data transfer between client and server. 
Applied to our use case the client would first setup a WebSocket connection to the server. Once the connection is established it sends a request for the report to be generated. The server on its turn would generate the report and only when the generation finishes send back the report download URL as a response, using the same connection.

## Proposed Design Second Approach using Aysch Lambda
---

![](https://user-images.githubusercontent.com/107042677/185735937-b753a250-6bae-47e6-844b-8f59dca844d1.png)

### How it's working:
---

Several AWS services, such as Amazon Simple Storage Service (Amazon S3) and Amazon Simple Notification Service (Amazon SNS), invoke functions asynchronously to process events. When you invoke a function asynchronously, you don't wait for a response from the function code. You hand off the event to Lambda and Lambda handles the rest. You can configure how Lambda handles errors, and can send invocation records to a downstream resource to chain together components of your application.

## Environment Setup
---

* First install Windows Subsystem for Linux (WSL). For this, download WSL.exe file from Google. I faced error in installtion using wsl --install command so I used wsl.exe --install -d Ubuntu-20.04 commad to install it correctly.
* Dwnloaded VS Code and setup remote WSL from windows
* Download python3
* Donwload awscliv2.zip file from given path and install AWS. If you download it directly from google, there will be issue of path.
* Download and install NVM and NPM Check versions of all to be sure that softwares are installed corrrectly.

## Project Deployment - How to Run
---

* Open the ubuntu terminal and clone the git repository using git clone forked-repo-github-url Confirm that your working directory is `Sprint5_day9`
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
