import boto3, logging, os

logger = logging.getLogger()
logger.setLevel(os.environ['loglevel'])
logger.debug('os.environ=%s' % os.environ)

def lambda_handler(event, context):

    logger.info('entering lambda_handler')
    code = 200
    result = '{"xss": "<script>alert(1);</script>"}'
    response = {
        "statusCode": code,
        "headers": {"content-type": "application/json"},
        "body": result
    }

    return response
