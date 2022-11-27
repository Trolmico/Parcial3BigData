import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Animales')

response = table.query(
    KeyConditionExpression=Key('indice').eq("Dog")
)

for i in response['Items']:
    print(i)