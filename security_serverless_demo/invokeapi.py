import boto3, logging, os, requests, json

logger = logging.getLogger()
logger.setLevel(os.environ['loglevel'])
logger.debug('os.environ=%s' % os.environ)

def lambda_handler(event, context):

    url=os.environ['apiurl']
    logger.info('trying %s' % url)
    try:
        apiresponse = requests.post(url)
        logger.info('response was: %s' % apiresponse.json())
        respjson = apiresponse.json()
        respstr = json.dumps(respjson)
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
        "headers": {"content-type": "application/json"},
        "body": respstr
    }
    logger.info("response = %s" % response)

    return response
