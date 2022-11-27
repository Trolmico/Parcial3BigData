import boto3
import json
from boto3.dynamodb.conditions import Key, Attr


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Animales')

fe = Key('indice').begins_with("T")
pe = "#idx, ruta, informacion"
ean = { "#idx": "indice", }
esk = None


response = table.scan(
    FilterExpression=fe,
    ProjectionExpression=pe,
    ExpressionAttributeNames=ean
    )
for i in response['Items']:
    print(json.dumps(i))