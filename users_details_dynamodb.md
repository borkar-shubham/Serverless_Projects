## Introduction
In this article we will focus in special AWS services who want to fast build and deploy endpoints, to GET/POST/PUT/DELETE information 
on a database regarding data of some application. The importance of server-less application are getting higher demand each day and aws 
available services offers a cheap and secured environment, so that the reason so many huge companies are migrating great part of their 
infrastructure to the cloud. We are using three awesome services API Gateway, Lambda and DynamoDB.

Lets start with Demo
Aim: To create an API with CRUD operation using following services -
* a. DynamoDB
* b. Lambda
* c. API gateway
* d. IAM Service

### Creating the DynamoDB Table:
* Table name : member_table
* Partition key : MemberId (String)

Create a Role & Policy
Before we go for Lambda to be able to access DynamoDB we need to give Lambda permission. Let’s create a new Policy.

In next page attach policy search for AMAzonDynamoDBFullAccess, api_excute, cloudfullacess, select that policy and click on next.

Enter role name and click create role.

Now attache this role to lambda function under the execution role select IAM role which you have created.

Create a Lambda Function
AWS Lambda is event-driven computing rather than an imperative model. Events-driven computing responds to events when the event source happens, it triggers the lambda function. The event source could be a request to an endpoint which we will go through later using API Gateway.

Search for lambda service

Double click on the lambda service and click on create function

There you select an author from scratch, give some function name and select the language as Nodejs

After selecting the required parameters click on create function. then you will be getting a code editor. there you write your nodejs code for get/put data from dynamo DB.

Screenshot 2022-02-28 at 1.08.04 AM.png

Function name: users_details_api

Runtime: Node.js 14.x

Execution role: Use an existing role

Role name: myServerlessRole

The handler method is the method that will be executed when the lambda function is invoked. This function takes in two objects, event and context.


Click on the Deploy button to deploy the Lambda function.

Create an API Gateway
When your API method receives an HTTP request, API Gateway invokes your Lambda function.

Create a REST API in API Gateway.

Open AWS Console, type API Gateway in the search bar, and hit enter.

Click on the Build button on REST API.

Fill in the details as below.

Choose the protocol: REST

Create new API: New API

API name: user-api

Endpoint Type: Regional

Select the Actions drop-down list, choose to Create Resource. Fill in the details as below.

Resource Name: users

Second Resource Name : user

Click on Create Resource button to complete. Select the Actions drop-down list again, choose Create Method. Select POST to insert a new record. Again repeat process for all methods Get, Update, DeleteScreenshot 2022-03-06 at 11.12.26 PM.png

Integration type: Lambda Function

Use Lambda Proxy integration: Checked(remember to check so event details will be passed to Lambda)

Lambda Function: users_details_api


Click the Save button, a message with Add Permission to Lambda Function will pop out, click OK to grant the permission.


Deploy the API
In the last step, we need to deploy the API so that we can access it thru the public. Click on the Actions drop-down list, select Deploy API.


Click the Deploy button and then the Save Changes button. An Invoke URL will appear on top. Try accessing the URL from the browser or Postman.

Test API using Postman
Copy the Invoke URL and paste in Postman Paste the test data to Request Body and click send.
```
{ "Name": "Christian", "Last Name": "Salazar", "Gender": "Male", "phone_number" : "9898989898" }
```

Verify the data in the DynamoDB table.
In conclusion, we have learned about creating a serverless CRUD API using AWS services such as Lambda, DynamoDB, and API Gateway.

