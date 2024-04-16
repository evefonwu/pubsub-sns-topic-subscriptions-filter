import os 
import boto3

'''
This lambda fn publishes a Hello message.
'''

sns = boto3.client('sns')

def lambda_handler(event, context):
  sns_topic_arn = os.environ.get('DEMO_SNS_TOPIC_ARN')
  print(sns_topic_arn)
  params = {
    'Message': 'Hello!',
    'TopicArn': sns_topic_arn,    
  }

  try: 
    response = sns.publish(**params)
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
  
  

