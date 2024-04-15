# SNS Subscription Filter Demo

This is the source code for the demo described in this post:

SNS Subscription Filter Demo

## To Deploy this CDKv2 Python Application

If you need a general CDK App Walkthrough Resource: [tutorial](https://docs.aws.amazon.com/cdk/v2/guide/serverless_example.html)

### Additional Steps:

### Activate environment variables

Create .env file with the following environment variables:

```
export IAC_PARAM_WELCOME_TEAM_EMAIL_ADDRESS=<enter-email-address>
export IAC_PARAM_EMAIL_ADDRESS=<enter-another>
```

```sh
source .env
```

`source` tells bash interpreter to read the .env file

`export` command makes the values available to the shell processes

### Deploy to AWS account/region

```sh
cdk deploy
```

`cdk deploy` provides a changeset, and when confirmed, deploys the infrastructure and runtime code together to the default AWS account/region configured in the local AWS CLI

### Confirm subscriptions

Confirm the email subscriptions in order to receive the SNS Topic messages published by lambda function URL invocations.
