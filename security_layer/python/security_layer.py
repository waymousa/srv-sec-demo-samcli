def getLogonInfo():
    print("getLogonInfo layer method called.")
    return 1
#    app.logger.debug('>>> Start Request.')
#    app.logger.debug('URL: %s', request.url)
#    app.logger.debug('Headers: %s', request.headers)
#    app.logger.debug('Cookies: %s', request.cookies)
#    app.logger.debug('x-amzn-oidc-accesstoken: %s', request.headers.get('x-amzn-oidc-accesstoken'))
#    app.logger.debug('x-amzn-oidc-identity: %s', request.headers.get('x-amzn-oidc-identity'))
#    app.logger.debug('x-amzn-oidc-data: %s', request.headers.get('x-amzn-oidc-data'))
#    if request.headers.get('x-amzn-oidc-data') is not None:
#        app.logger.debug('Found an odic data header to process')
#        encoded_jwt = request.headers.get('x-amzn-oidc-data')
#        jwt_headers = encoded_jwt.split('.')[0]
#        app.logger.debug('jwt_headers: %s', jwt_headers)
#        decoded_jwt_headers = base64.b64decode(jwt_headers)
#        app.logger.debug('decoded_jwt_headers: %s', decoded_jwt_headers)
#        decoded_jwt_headers = decoded_jwt_headers.decode("utf-8")
#        app.logger.debug('decoded_jwt_headers: %s', decoded_jwt_headers)
#        decoded_json = json.loads(decoded_jwt_headers)
#        app.logger.debug('decoded_json: %s', decoded_json)
#        kid = decoded_json['kid']
#        app.logger.debug('kid: %s', kid)
#        url = 'https://public-keys.auth.elb.us-east-1.amazonaws.com/' + kid
#        app.logger.debug('url: %s', url)
#        req = requests.get(url)
#        app.logger.debug('req: %s', req)
#        pub_key = req.text
#        app.logger.debug('pub_key: %s', pub_key)
#        payload = jwt.decode(encoded_jwt, pub_key, algorithms=['ES256'])
#        app.logger.debug('payload: %s', payload)
#    app.logger.debug('Body: %s', request.get_data())
#    app.logger.debug('<<< Finish Request.')