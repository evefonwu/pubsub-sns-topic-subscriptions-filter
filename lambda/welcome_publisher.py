import os 
import boto3

'''
This lambda fn demonstrates publishing an message with message attributes to an SNS Topic, with which to filter messages for different subscriptions. 

This lambda sends the account_created event for the demo application.
'''

sns = boto3.client('sns')

def lambda_handler(event, context):
  
  # boto3 sns.publish 
  # takes object with the key parameters, Message, TopicArn, MessageAttributes
  sns_topic_arn = os.environ.get('DEMO_SNS_TOPIC_ARN')
  print(sns_topic_arn)
  params = {
    'Message': 'Hello! A new account was created.',
    'TopicArn': sns_topic_arn,
    'MessageAttributes': {
        'application': {
          'DataType': 'String',
          'StringValue': 'demo'
        },
        'event': {
          'DataType': 'String',
          'StringValue': 'account_created'
        }
      }
  }
  try: 
    response = sns.publish(**params)

    # boto3 response returns an object with key, MessageId, etc.
    message_id = response.get('MessageId')
    if message_id:
      print(f"Published message. Message ID: {message_id}")
      return {
        'MessageId': message_id
      }
    else:
      print(f"Failed to publish to SNS Topic: {sns_topic_arn}")

  except Exception as e:
    print(f"Failed sns.publish: {e}")
  
  

