import os
import boto3

dynamodb = boto3.resource('dynamodb', region_name=os.getenv('AWS_REGION', 'ap-south-1'))
table = dynamodb.Table(os.getenv('NORTHWIND_TABLE', 'Northwind'))
