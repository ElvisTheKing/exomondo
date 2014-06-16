import requests
import logging
import uuid
import re

class Api(object):
    def __init__(self, 
                email = None, 
                password = None, 
                user_agent = None, 
                auth_token = None):
        
        if email and password:
            self.email = email
            self.password = password
        
        self.session = requests.Session()
        if user_agent:
            self.session.headers.update({'User-Agent': user_agent})

        if (not auth_token):
            if not (email and password):
                raise Exception('you should specify email and password or auth token')
            self.auth_token = self.request_auth_token()
        else:
            self.auth_token = auth_token

    def request_auth_token(self):
        url = 'https://api.mobile.endomondo.com/mobile/auth'
        params = { 
            'action': 'pair',
            'email':    self.email,
            'password': self.password,
            'country': 'GB',
            'deviceId': str(uuid.uuid4())
        }

        r = self.session.get(url,params = params)
        if (r.text.strip()[:2] != "OK"):
            raise Exception("auth token request failed", r.text)

        m = re.search(r'authToken=(.+)',r.text)
        logging.debug('Got auth token from endomondo: %s' % m.group(1))
        return m.group(1)

    def get_workouts(self, limit, fields = ['basic']):
        url = 'https://api.mobile.endomondo.com/mobile/api/workouts'
        params = {
            'authToken': self.auth_token,
            'fields': ','.join(fields),
            'maxResults': limit
        }

        r = self.session.get(url,params = params)
        workouts = r.json()['data']

        return workouts
