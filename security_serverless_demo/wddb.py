import logging, os, boto3, urllib, uuid, json

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
        logger.debug('got event{}'.format(event)) 
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(os.environ['table']) 
        body=event['body']
        logger.debug('body=%s' % body)
        body=urllib.parse.parse_qs(body)
        logger.debug('transformed_body=%s' % body) 
        firstname=body['firstname']
        firstname=firstname[0]
        logger.debug('firstname=%s' % firstname)
        surname=body['surname']
        surname=surname[0]
        logger.debug('surname=%s' % surname)
        email=body['email']
        email=email[0]
        logger.debug('email=%s' % email)
        #email = '<a href="mailto:' + email + '">' + email + '</a>'
        #logger.debug('email=%s' % email)
        myuuid=str(uuid.uuid4())
        logger.debug('uuid=%s' % myuuid)
        response=table.put_item(Item={"uuid":myuuid,"firstname":firstname,"surname":surname,"email":email})
        logger.debug('put_item suceeded.')

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
                "Access-Control-Allow-Origin": "https://diq3qr0d5ppph.cloudfront.net",
                "Content-Type": "application/json"
                },
            "body": json.dumps(response)
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
            "body": "Unauthorized"
        }




