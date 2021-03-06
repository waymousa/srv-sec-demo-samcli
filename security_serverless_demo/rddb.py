import boto3, logging, html, os, json
from json2html import *

logger = logging.getLogger()
logger.setLevel(os.environ['loglevel'])
logger.debug('os.environ=%s' % os.environ)

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table = dynamodb.Table(os.environ['table'])

    # fetch all todos from the database
    result = table.scan()

    logger.debug('result_set=%s' % result)

    items = json.dumps(result['Items'])

    logger.debug('result_items=%s' % items)

    table = json2html.convert(json = items)

    logger.debug('table=%s' % table)

    table = html.unescape(table)

    logger.debug('unecoded_table=%s' % table)
    # create a response
    
    #response = {
    #    "statusCode": 200,
    #    "body": json.dumps(result['Items'])
    #}

    #itemslist = []
    #itemsdict = {}

    #for i in result['Items']:
    #    itemsdict = json.loads(i)
    #    newitems.append(itemsdict)    

        # print(json.dumps(i, cls=DecimalEncoder))
    


    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
            "Access-Control-Allow-Origin": "https://diq3qr0d5ppph.cloudfront.net",
            "Content-Type": "application/json"
            },
        "body": table
    }

    return response
