# Webapp5:
deploy web application with aws lambda

## Create IAM Role
You start with creation of the IAM role which AWS Lambda function uses for the authorization to call other AWS Services.

1. Login to the AWS Console. Select Ireland as the region.
2. Goto the IAM Management console and click on the Roles menu in the left and then click on the Create role button.
3. On the next screen, select Lambda as the service and click on the Next: Permissions button.
4. On the next screen, select PowerUserAccess as the policy and click on the Next: Tags button.
5. On the next screen, click on the Next: Review button.
6. On the next screen, type in squarelambdarole for the Role name and click on the Create role button.
7. The role is created in no time. The next step is to create the lambda function.

## Create Lambda Function
You create the Lambda Function which hosts the business logic code and HTML user interface for the web application.

1. In the Lambda Console, click on the Functions menu in the left and then click on the Create function button
2. On the next screen, select Author from scratch as the option. Type in squarewebapp as the name. Select Python 3.9 as the runtime. Select Use an existing role as the option for the execution role and select squarelambdarole for the role. Finally, click on the Create function button.
3. The function is created in no time. You will configure Lambda function using code provided with this workshop. Download the function code webapp5.zip. Click on the Upload from button and then click on the .zip file option.
4. The Lambda function is ready. Let’s now configure API Gateway using Lambda as the backend.

## Create API Gateway
In this step, you configure REST API in API Gateway which calls Lambda function as the backend. The URL of the API becomes the URL of the web application.

1. In the API Gateway Console, click on the Build button for the REST API.
2. On the next screen, select REST for the protocol and select New API option. Type in squarewebapi for the API Name and select Regional for the endpoint type. Finally, click on the Create API button.
3. The API is created in no time. On the next screen, click on the Create Method option under the Action menu.
4. On the next screen, select GET as the method and click on the confirmation icon.
5. The method is created in no time. On the next screen, select Lambda Function option for the integration type. Select Use Lambda Proxy integration option. Select squarewebapp for the Lambda Function. Keep rest of the configuration to the default and click on the Save button.
6. It will throw a popup asking API Gateway permission to call the Lambda function. Click on the OK button.
7. The GET method is updated. You repeat the same steps to create a POST method as well. Click on the Create Method option under the Action menu.
8. The POST method is updated. Go back to the API details and click on the Deploy API option under the Action menu.
9. It will throw popup to configure the deployment stage. Select [New Stage] as the deployment stage. Type in app for the stage name and click on the Deploy button.
10. The API is deployed to the dev stage. Make note of the Invoke URL. You will need it later when testing the API.
11. The API is deployed and ready. It will render the web application. Let’s test it in the next step.
    
## Test Web Application
The web application is deployed using Amazon API Gateway. Let’s test it.
1. Open Web Browser and navigate to the Invoke URL of the API.