# Design & Develop Day 12 Project
---

### Design Problem Statement:
---
Tourism is usually the pillar industry of many countries because it has many benefits for improving
the national economy and political exchanges. Design a travel-oriented application that provides
customized and personalised service. The application should advise and help create a personalized
travel itinerary for tourists based on their purpose of visit (exploring, unwind, relaxation, adventure, student trip, business), interests, number of days staying, and financial constraints. The application should essentially help them filter attractions at their potential destination based on personal information entered by them. For example, some tourists may be in Sydney to explore, while others may be there to unwind and relax, while others might prefer a mix of both. Another example is that some tourists might be interested in experiencing Japan's Cherry Blossom season. In this case, the application should suggest the best time to visit Japan to experience this season is in the spring. It should assist them by suggesting the best parks to visit based on their budget and the number of days they are available, or in other words, their available time. Additionally, the application should assist in choosing the best accommodation and all other necessary facilities (such as restaurants and more) by recommending the best ones that fit their budget and were close to the parks.

## Proposed Design 
---

![](https://user-images.githubusercontent.com/107042677/185783583-95ada2d7-d073-4965-bb8a-48b5b6f82162.png)

## Core Features of App
---

* Searching menu: Allow your users to search for different restaurants, cafes by location, and cuisines. Using the search filter, users can easily find their favorite eating places, list menu, offers, etc.
* Order placement: The user can place an order of selected dishes and food. They just need to cross-verify their preferred dish, delivery time, and proceed check-out.
* Payment gateway integration: You provide the users with multiple payment options like credit/debit cards, different wallets like Google Pay, Paytm, Phonepe, UPI, etc

## Application Flow
---

We are considering here microservices-based architecture. Different services are listed in the architecture diagram

* 1: All requests made from a mobile app or UI will go to different services via the API gateway. API gateway will take care of load balancing and routing requests to services. This will authenticate and authorize the user and send back the token ID. This token is used for further communication
Different services like, user registration and management service, order service, payment service will use transactional databases. We will use the Amazon Aurora relational database. This is a highly scalable database service to manage users and concurrent orders etc.

* 2: Information about different restaurants, their menu, price, offers, weathers etc will be stored in JSON document storage in ElasticSearch. We can use a multi-node cluster here. Whenever a customer searches for a menu/cuisines it will be fetched from elastic search. Elastic search provides fast scalable search options

* 3: Once the user selects the dishes and quantity from the restaurant, select his tour plan, select different location etc. He will go to the checkout option and then do payment. Different payment gateways and payment options are integration with the system and upon successful payments, the order is successfully placed

* 4: Once the order is placed all the information is sent to the central message Queue like Kafka. The order processing unit reads the order info and then notifies the selected restaurant about the order. At the same time, it searches for available delivery partners to nearby locations to pick up the order. It also gets the information like preparation time from the restaurant and estimated pickup time from the delivery partner based on his location and other details. 

* 5: The user gets push notification about the order. The order processing and tracking service will work together and the user can track their order status, etc


## Delivery Engine
---

This will read information like food preparation time, time to reach to the customer place, historic data about last orders, delivery time and predict the delivery times for orders based on historical data and real-time data like maps data, current delivery person data, etc. This will also take care of assigning delivery persons for orders. This keeps on updating the pool of delivery persons for given locations.

## Easy onboarding and Searchability of Restaurant
---

From the Admin panel, the admin can add the restaurant. Admin adds details like restaurant name, city, address, postal code, cuisine type, operational hours, owner details, payment shares, etc. All this information is stored in a relational database. We use Amazon Aurora here.

Once the restaurant is added we will generate a Unique ID for the restaurant. This unique ID will be used in Elastic search to store information like different menus, their price, preparation time, etc.

Restaurants have access to add /update/delete menu, price, preparation time, etc

So when a customer searches food options by dish name, restaurant name, location then ElasticSearch is queried. Elasticsearch is a highly available, scalable open-source full-text search and analytics engine. With elastic search, you can store, analyze, search large volumes of data quickly and in near realtime.

## Environment Setup
---

* First install Windows Subsystem for Linux (WSL). For this, download WSL.exe file from Google. I faced error in installtion using wsl --install command so I used wsl.exe --install -d Ubuntu-20.04 commad to install it correctly.
* Dwnloaded VS Code and setup remote WSL from windows
* Download python3
* Donwload awscliv2.zip file from given path and install AWS. If you download it directly from google, there will be issue of path.
* Download and install NVM and NPM Check versions of all to be sure that softwares are installed corrrectly.

## Project Deployment - How to Run
---

* Open the ubuntu terminal and clone the git repository using git clone forked-repo-github-url Confirm that your working directory is `Sprint5_day12`
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
