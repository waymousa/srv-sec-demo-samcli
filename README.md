# serverless-security-demo

This application demonstrates some of the security vulnerabilities that can be introduced to your Serverless Applications.

## Prerequisites

It is assumed you have a working knowlege of AWS Lambda, API Gateway, Cognito and DynamoDb.  The Lambda functions are written in Python for the 3.8 runtime. The UI is written in html, javascript and css. You will also need the sam-cli and aws-cli installed as well as an aws-cli profile with admin rights to an AWS account.

## Download, Build and Deploy

Fork this repo and git clone it locally usign the IDE of your choice.

To build the project you will need to edit the template.yaml file and change the metadata section details to match your own name and repo urls

```bash
Metadata:
  AWS::ServerlessRepo::Application:
    Name: serverless-security-demo
    Description: Simple serverless application to demonstrate security concepts
    Author: YOUR_NAME_HERE
    SpdxLicenseId: Apache-2.0
    LicenseUrl: LICENSE.txt
    ReadmeUrl: README.md
    Labels: ['tests']
    HomePageUrl: YOUR_REPO_HERE
    SemanticVersion: 0.0.1
    SourceCodeUrl: YOUR_REPO_HERE
```

Next, run the sam-cli to build and deploy the project.  Follow the prompts as directed.

```bash
sam build
sam deploy
```

You should no be able to see the resources created byu the CloudFormation template in your account.  Before you can use the application you must make a few changes.

1. Create an S3 bucket to hold the static content.  Upload the static content there.
2. Create a Cloudfront distribution with the S3 bucket above as the origin.
3. Update the user pool by setting the domain name for your user pool.
4. Update the app client to use the DNS for the CloudFront distribtuion for the redirect urls.
5. Edit the Javascript and update the variables at the top of the script with the values for your Cognito user pool, domain name and CloudFront DNS name.
6. Update the Lambda functions to use the CLoudFront DNS name for the CORS header.
7. Update the first user account password so its ready to use.
8. Create home, secret and admin groups and add the user to all those groups.

You should now be able to logon and try the home page.