import boto3, logging, os, subprocess, urllib, json

logger = logging.getLogger()
logger.setLevel(os.environ['loglevel'])
logger.debug('os.environ=%s' % os.environ)

#function_shield.configure({
#    "policy": {
       # 'block' mode => active blocking
       # 'alert' mode => log only
       # 'allow' mode => allowed, implicitly occurs if key does not exist
#        "outbound_connectivity": os.environ['FUNCTION_SHIELD_OUTBOUND_CONNECTIVITY'],
#        "read_write_tmp": os.environ['FUNCTION_SHIELD_READ_WRITE_TMP'],
#        "create_child_process": os.environ['FUNCTION_SHIELD_CREATE_CHILD_PROCESS']
#    },
#    "token": os.environ['FUNCTION_SHIELD_TOKEN']
#})

def lambda_handler(event, context):

    logger.info('request started')
    body=event['body']
    logger.debug('body=%s' % body)
    logger.debug('context=%s' % context)
    groups=event['requestContext']['authorizer']['claims']['cognito:groups']
    logger.debug('groups=%s' % groups)
    sub=event['requestContext']['authorizer']['claims']['sub']
    logger.debug('sub=%s' % sub)
    body=urllib.parse.parse_qs(body)
    logger.debug('transformed_body=%s' % body)
    cmd=body['command']
    cmd=cmd[0]
    logger.info('cmd=%s' % cmd)

    if "admin" in groups:
        logger.debug('sub %s is authorised.' % sub)

        try:

            logger.debug('entering try block...')
            result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
            logger.debug('result = %s ' % result)
            result = result.decode('utf-8')
            result = json.dumps(result)
            logger.info('result=%s' % result)
            result = '{"result":%s}' % (result)
            response = {
                "statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
                    "Access-Control-Allow-Origin": "https://diq3qr0d5ppph.cloudfront.net",
                    "content-type": "text/html"
                    },
                "body": result
            }

        except subprocess.CalledProcessError as e: 

            logger.debug('capturing a CalledProcessError...')
            logger.error('return code=%s' % e.returncode)
            logger.error('cmd=%s' % e.cmd)
            logger.error('output=%s' % e.output)
            output = e.output.decode('utf-8')
            output = json.dumps(output)
            result = '{"returncode":"%s", "cmd":"%s", "output":%s}' % (e.returncode, e.cmd, output)
            response = {
                "statusCode": 500,
                "headers": {"content-type": "application/json"},
                "body": result
            }

        except Exception as e:
            logger.debug('capturing a general Exception...')
            logger.error('exception=%s' % e, exc_info=True)
            result = '{"exception type":"%s"}' % (e)
            code = 500
            response = {
                "statusCode": code,
                "headers": {
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
                    "Access-Control-Allow-Origin": "https://diq3qr0d5ppph.cloudfront.net",
                    "Content-Type": "application/json"
                    },
                "body": result
            }

        logger.info("response=%s" % response)
        return response

    else:
        logger.debug('sub %s is unauthorised.' % sub)
        response = {
            "statusCode": 403,
            "headers": {
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
                "Access-Control-Allow-Origin": "https://diq3qr0d5ppph.cloudfront.net",
                "Content-Type": "text/html"
            },
            "body": "Unauthorized"
        }        

        return response