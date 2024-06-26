# SNS Topic Subscriptions Filter Demo

Demo of an Amazon Simple Notification Service (SNS) topic with multiple email subscriptions and how to add subscription filtering in SNS.

## Steps

### Requirements

Requirements for any CDK app, in general, check out: [Getting Started with the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)

Specific to CDK apps in Python: [Working with the AWS CDK in Python
](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html)

### Clone the repository

cd into the project

### Create a virtual environment with venv

```sh
python3 -m venv .venv
```

### Activate venv environment

```sh
source .venv/bin/activate
```

### Install package dependencies

This repo requires aws-cdk-lib 2.137.0. See requirements.txt for package dependencies.

Install into the venv virtual environment for this project:

```sh
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

`cdk deploy` initiate deploying to the default AWS account/region configured with the AWS CLI

### Confirm subscriptions

Confirm the email subscriptions in order to receive the SNS Topic messages published by lambda function URL invocations.

## Blog post and Resource links:

[EDA Messaging: SNS Topic Subscriptions Filter Demo](https://dev.to/evefonwu/eda-messaging-sns-topic-subscriptions-filter-demo-5cf8)
