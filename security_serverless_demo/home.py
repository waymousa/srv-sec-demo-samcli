import json
import security_layer as security_layer

# import requests


def lambda_handler(event, context):

    respjson = { 
        "layer": security_layer.getLogonInfo(), 
        "message": "hello world"
    } 

    longinformation = '''
    <head>
    <meta charset="UTF-8">
    <title>Amazon Cognito Credentials Example</title>
    <meta charset="utf-8">
    <script src="./main.ts"></script>
    <script>
      showId();
    </script>
    </head>
    <html>
    <body onload="showId();">
    <h1>Hello world</h1>
    <p>This site is a prototype API which does little.</p>
    <h1>Login</h1>
    <a href="https://srv-sec-semo-875667080425.auth.us-east-1.amazoncognito.com/login?response_type=token&client_id=13plluo9hsnmpaosrrce2rf65k&redirect_uri=https://c19g7smvpc.execute-api.us-east-1.amazonaws.com/Dev/">Login</a>
    <h1>Logout</h1>
    <a href="https://srv-sec-semo-875667080425.auth.us-east-1.amazoncognito.com/logout?client_id=13plluo9hsnmpaosrrce2rf65k&logout_uri=https://c19g7smvpc.execute-api.us-east-1.amazonaws.com/Dev/">Logout</a>
    <h1>Secret</h1>
    <a href="/secret">Secret</a>
    <div id="results">data</div>
    </html>
    '''

    return {
        "statusCode": 200,
        "headers": {
          "Access-Control-Allow-Headers": "Content-Type",
          "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
          "Access-Control-Allow-Origin": "https://diq3qr0d5ppph.cloudfront.net"
        },
        
        "body": json.dumps(respjson)
    }
