import json
import boto3

ses = boto3.client('ses')

def handler(event, context):
    for record in event['Records']:
        message = json.loads(record['body'])
        email = message['email']
        unit_id = message['unit_id']
        timestamp = message['timestamp']

        ses.send_email(
            Source='your-email@example.com',
            Destination={'ToAddresses': [email]},
            Message={
                'Subject': {'Data': 'Storage Unit Accessed'},
                'Body': {'Text': {'Data': f"Your unit {unit_id} was accessed at {timestamp}."}}
            }
        )
    return {"statusCode": 200}
