
# **Welcome to My First Desing CDK Python project!**
---
## Design 1 Problem Statement:
Design & Develop - Consider that you are getting an event response as {“arg1”: 10} from an API.
* Make an AWS app that generates an alarm if arg1 > 10.    
* When the alarm is raised, sends an email to a dummy account.

## Design of Problem 1
Given below is the design for the problem 1.
![](https://user-images.githubusercontent.com/107042677/185744655-cd22b176-6c86-44ca-9f89-ee3fe4570c3c.png)

## Explanation
So here you can see that client is abale to put an argument value via `API GATEWAY`, which will generate a request by invoking the lambda function only if argumnet value is greater than 10. 
After that it will generate the alarm and send an email notification to a dummy account as well.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
