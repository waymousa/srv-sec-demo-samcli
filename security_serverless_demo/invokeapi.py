import boto3, logging, os, requests, json, urllib

logger = logging.getLogger()
logger.setLevel(os.environ['loglevel'])
logger.debug('os.environ=%s' % os.environ)

def lambda_handler(event, context):

    logger.info('request started')
    logger.debug('event=%s' % event)
    logger.debug('context=%s' % context)
    body=event['body']
    logger.debug('body=%s' % body)
    body=urllib.parse.parse_qs(body)
    logger.debug('transformed_body=%s' % body)
    groups=event['requestContext']['authorizer']['claims']['cognito:groups']
    logger.debug('groups=%s' % groups)
    sub=event['requestContext']['authorizer']['claims']['sub']
    logger.debug('sub=%s' % sub)

    if 'secret' in groups:
        logger.debug('sub %s is authorised.' % sub)
        url=body['invokeapi']
        url=url[0]
        #url=os.environ['apiurl']
        logger.info('trying %s' % url)
        try:
            apiresponse = requests.post(url)
            #logger.info('response was: %s' % apiresponse.json())
            #respjson = apiresponse.json()
            #respstr = json.dumps(respjson)
            respstr = apiresponse.text
            logger.info('respstr is: %s' % respstr)
            code = 200
        except OSError as e:
            logger.error('exception=%s' % e, exc_info=True)
            return strings.bad_response
        except Exception as e:
            logger.error('exception=%s' % e, exc_info=True)
            respstr = '{"exception type":"%s"}' % (e)
            code = 500

        response = {
            "statusCode": code,
            "headers": {
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
                "Access-Control-Allow-Origin": "https://diq3qr0d5ppph.cloudfront.net",
                "Content-Type": "text/html"
            },
            "body": respstr
        }
        logger.info("response = %s" % response)

        return response

    else:
        logger.debug('sub %s is unauthorised.' % sub)
        return {
            "statusCode": 403,
            "headers": {
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
                "Access-Control-Allow-Origin": "https://diq3qr0d5ppph.cloudfront.net",
                "Content-Type": "text/html"
                },
            "body": "Unauthorized"
        }


    
