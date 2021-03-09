import boto3, logging, os

logger = logging.getLogger()
logger.setLevel(os.environ['loglevel'])
logger.debug('os.environ=%s' % os.environ)

def lambda_handler(event, context):

    logger.info('entering lambda_handler')
    logger.debug('event=%s' % event)
    logger.debug('context=%s' % context)
    code = 200
    result = '<a href="javascript:alert(\'Happy days!\');">Click here</a>'
    response = {
        "statusCode": code,
        "headers": {"content-type": "application/json"},
        "body": result
    }

    return response
