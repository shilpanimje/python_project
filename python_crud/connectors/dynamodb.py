"""DynamoDb Connector.

Manages connection to DynamoDb.
"""
import boto3

dynamodb_resource = boto3.resource('dynamodb')
