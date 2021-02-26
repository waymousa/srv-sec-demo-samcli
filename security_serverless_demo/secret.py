import json
import security_layer as security_layer

# import requests


def lambda_handler(event, context):

    respjson = { 
        "layer": security_layer.getLogonInfo(), 
        "message": "secret page"
    }

    return {
        "statusCode": 200,
        "headers": {
          "Access-Control-Allow-Headers": "Content-Type",
          "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
          "Access-Control-Allow-Origin": "https://diq3qr0d5ppph.cloudfront.net"
        },
        
        "body": json.dumps(respjson)
    }
