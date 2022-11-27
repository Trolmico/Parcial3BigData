import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.create_table(
    TableName='Animales',
    AttributeDefinitions=[
        {
            'AttributeName': 'indice',
            'AttributeType': 'S'  
        },
        {
            'AttributeName': 'ruta',
            'AttributeType': 'S'
        },
    ],
    KeySchema=[
        {
            'AttributeName': 'indice',
            'KeyType': 'HASH'  
        },
        {
            'AttributeName': 'ruta',
            'KeyType': 'RANGE'  
        },
    ],
    
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

