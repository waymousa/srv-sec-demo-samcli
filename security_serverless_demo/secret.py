import json
import security_layer as security_layer

# import requests


def lambda_handler(event, context):
    
    security_layer.getLogonInfo()

    longinformation = '''
    <html>
    <h1>SECRET PAGE</h1>
    <p>This is a secret page.</p>
    <h1>Home</h1>
    <a href="https://c19g7smvpc.execute-api.us-east-1.amazonaws.com/Dev/">Home</a>
    </html>
    '''

    return {
        "statusCode": 200,
        "headers": {'Content-Type': 'text/html'},
        "body": longinformation
    }
