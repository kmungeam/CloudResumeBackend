import json
import boto3

def lambda_handler(event, context):
    # connect to DynamoDB resource
    client = boto3.resource('dynamodb')
    # create a DynamoDB client to the visitor_count table
    table = client.Table('visitor_count')
    # increment visitor_count attribute for index.html key
    response = table.update_item(
        Key={
            'path': 'index.html'
        },
        AttributeUpdates={
            'visitor_count':{
                'Value': 1,
                'Action': 'ADD'
            }
        }
    )
    # get updated visitor_count
    response = table.get_item(
        Key={
            'path': 'index.html'
        }
    )
    # return visitor count to user
    
    visitor_count = response['Item']['visitor_count']
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': visitor_count
    }
