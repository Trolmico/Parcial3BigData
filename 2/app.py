#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

def save_to_database(item):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Animals')
    response = table.put_item(
    Item=item
    )
    return response

def handler(event,context):
    bucket= event['Records'][0]['s3']['bucket']['name']
    foto=event['Records'][0]['s3']['object']['key']
    client=boto3.client('rekognition',region_name='us-east-1')

    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':foto}},
        MaxLabels=10)


    labels= response["Labels"]
    item = {}
    item["indice"]=labels[0]["Name"]
    info=[]
    for label in labels:
        info.append(label["Name"])
    item ["informacion"]=info
    item["ruta"]=foto
    
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Animales')
    response = table.put_item(
    Item=item
    )
    return response