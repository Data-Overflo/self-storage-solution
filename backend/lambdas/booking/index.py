import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('BookingTable')

def handler(event, context):
    if event['httpMethod'] == 'POST':
        body = json.loads(event['body'])
        booking_id = body['booking_id']
        customer_name = body['customer_name']
        facility_id = body['facility_id']
        unit_type = body['unit_type']
        start_date = body['start_date']
        end_date = body.get('end_date', 'indefinite')

        table.put_item(
            Item={
                'BookingID': booking_id,
                'CustomerName': customer_name,
                'FacilityID': facility_id,
                'UnitType': unit_type,
                'StartDate': start_date,
                'EndDate': end_date,
                'Status': 'Reserved'
            }
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Booking successful!"})
        }
