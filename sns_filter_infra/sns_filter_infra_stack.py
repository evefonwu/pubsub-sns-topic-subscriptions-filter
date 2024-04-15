import os 
from aws_cdk import (
    Stack,
    CfnOutput,
    aws_sns as sns,
    aws_sns_subscriptions as sub,
    aws_lambda as _lambda, 
)
from constructs import Construct

# a subclass of Stack to create infra resources in CDK
class SnsFilterInfraStack(Stack):

    # constructor method
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        WELCOME_TEAM_EMAIL_ADDRESS = os.environ.get("IAC_PARAM_WELCOME_TEAM_EMAIL_ADDRESS")
        print(WELCOME_TEAM_EMAIL_ADDRESS)
        
        EMAIL_ADDRESS = os.environ.get("IAC_PARAM_EMAIL_ADDRESS")
        print(EMAIL_ADDRESS)

        # Resources: SNS email subscriptions, one with a filter policy        
        welcome_team = sub.EmailSubscription(email_address=WELCOME_TEAM_EMAIL_ADDRESS,
            filter_policy={
                "application": sns.SubscriptionFilter.string_filter(
                    allowlist=["demo"]
                ),
                "event": sns.SubscriptionFilter.string_filter(
                    allowlist=["account_created"]
                )
            }) 
        demo = sub.EmailSubscription(email_address=EMAIL_ADDRESS)

        # Resource: An SNS topic with email subscriptions
        sns_topic = sns.Topic(self, "DemoSNSTopic")
        sns_topic.add_subscription(welcome_team)
        sns_topic.add_subscription(demo)
        
        # Resources: Lambda functions configured with function URLS
        current_dir = os.path.dirname(__file__)
        lambdaDirectory = os.path.join(current_dir, '../lambda')

        # publisher to send notification to welcome team
        welcome_publisher_fn = _lambda.Function(self, "WelcomePublisherFn",
            code=_lambda.Code.from_asset(lambdaDirectory),
            handler="welcome_publisher.lambda_handler",
            runtime=_lambda.Runtime.PYTHON_3_12,
            environment={
                'DEMO_SNS_TOPIC_ARN': sns_topic.topic_arn
            }
        )        
        welcome_fn_url = welcome_publisher_fn.add_function_url(
            auth_type=_lambda.FunctionUrlAuthType.NONE,
            cors=_lambda.FunctionUrlCorsOptions(
                allowed_origins=["*"], # default No origins allowed
                allowed_methods=[_lambda.HttpMethod.ALL],
                allowed_headers=["*"]
            )
        )

        # publisher to send general messages
        publisher_fn = _lambda.Function(self, "PublisherFn",
            code=_lambda.Code.from_asset(lambdaDirectory),
            handler="publisher.lambda_handler",
            runtime=_lambda.Runtime.PYTHON_3_12,
            environment={
                'DEMO_SNS_TOPIC_ARN': sns_topic.topic_arn
            }
        )        
        fn_url = publisher_fn.add_function_url(
            auth_type=_lambda.FunctionUrlAuthType.NONE,
            cors=_lambda.FunctionUrlCorsOptions(
                allowed_origins=["*"], 
                allowed_methods=[_lambda.HttpMethod.ALL],
                allowed_headers=["*"]
            )
        )
        
        # Permissions: grant lambda permission to publish to the sns_topic 
        sns_topic.grant_publish(welcome_publisher_fn)
        sns_topic.grant_publish(publisher_fn)

        # Cfn Output
        CfnOutput(self, "SNSTopic_ARN", value=sns_topic.topic_arn)        
        CfnOutput(self, "WelcomePublisherFn_URL", value=welcome_fn_url.url)
        CfnOutput(self, "PublisherFn_URL", value=fn_url.url)