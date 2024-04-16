# EDA PubSub Messaging: SNS Subscriptions Filter Demo

This is the CDK Python Application source code for the demo described in this post:

SNS Subscriptions Filter Demo

Pre-requisites. For system requirements to deploy CDK applications, check out: [Tutorials](https://docs.aws.amazon.com/cdk/v2/guide/serverless_example.html)

## Steps

### Clone the repository

### Activate virtual environment and install the dependencies

```sh
source .venv/bin/activate
pip install -r requirements.txt
```

### Create .env file with your variable values

```
export IAC_PARAM_WELCOME_TEAM_EMAIL_ADDRESS=
export IAC_PARAM_EMAIL_ADDRESS=
```

### Activate environment variables

```sh
source .env
```

`source` tells bash interpreter to execute the commands in the file

`export` makes the value available to the shell processes

### Deploy to AWS account/region

```sh
cdk deploy
```

`cdk deploy` provides a changeset, when confirmed, deploys the infrastructure and runtime code together to the default AWS account/region configured with the AWS CLI

### Confirm subscriptions

Confirm the email subscriptions in order to receive the SNS Topic messages published by lambda function URL invocations.
