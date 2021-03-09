import json, logging, os
import security_layer as security_layer

logger = logging.getLogger()
logger.setLevel(os.environ['loglevel'])
logger.debug('os.environ=%s' % os.environ)

def lambda_handler(event, context):

    logger.info('request started')
    logger.debug('event=%s' % event)
    logger.debug('context=%s' % context)
    groups=event['requestContext']['authorizer']['claims']['cognito:groups']
    logger.debug('groups=%s' % groups)
    sub=event['requestContext']['authorizer']['claims']['sub']
    logger.debug('sub=%s' % sub)

    if 'secret' in groups:
        logger.debug('sub %s is authorised.' % sub)
        respjson = { 
            "layer": security_layer.getLogonInfo(), 
            "message": "here's some secret information."
        }

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
                "Access-Control-Allow-Origin": "https://diq3qr0d5ppph.cloudfront.net",
                "Content-Type": "application/json"
            },
        
            "body": json.dumps(respjson)
        }

    else:
        logger.debug('sub %s is unauthorised.' % sub)
        return {
            "statusCode": 403,
            "headers": {
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
                "Access-Control-Allow-Origin": "https://diq3qr0d5ppph.cloudfront.net",
                "Content-Type": "application/json"
            },
        
            "body": "Unauthorised"
        }
