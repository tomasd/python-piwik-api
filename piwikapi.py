import simplejson
import requests

__all__ = ['PiwikAPI']

class PiwikAPI(object):
    '''
        Usage: 
        PIWIK_URL = 'http://demo.piwik.org/'
        PIWIK_TOKEN = '53983b97138c69b72b0a32bbfeedc213'
        
        piwik = PiwikAPI(PIWIK_URL, PIWIK_TOKEN)
        piwik.SitesManager.getAllSites()
        piwik.UsersManager.getUser(userLogin='tomas4')
    '''
    def __init__(self, url, token_auth=None):
        self.url = url
        self.token_auth = token_auth
        
        
    def __getattr__(self, name):
        return PiwikManager(self, name)
    
class PiwikManager(object):
    def __init__(self, api, name):
        self.api = api
        self.name = name
        
    def __getattr__(self, name):
        def call_piwik(*args, **kwargs):
            if args:
                raise Exception('All piwik parameters should be explicitly named')
            return self.__call(name, **kwargs)
        return call_piwik
    
    
    def __call(self, method, format='json', **kwargs): #@ReservedAssignment
        method = '%s.%s' % (self.name, method)
        
        args = {'module' : 'API',
                'method' : method,
                'format' : format, }
        
        if self.api.token_auth:
            args['token_auth'] = self.api.token_auth
            
        args.update(kwargs)
        for key in args:
            if isinstance(args[key], list):
                args[key] = map(str, args[key])
                args[key] = ','.join(args[key])
                
        response = requests.get(self.api.url,
                                params=args,
                                headers={'User-Agent' : 'Python PiwikAPI'})
        
        if response:
            data = response.text
        else:
            raise PiwikError('Piwik returned status code of %d, error: %s' 
                             % (response.status_code, response.error))
            
        if data is not None and format == 'json':
            data = simplejson.loads(data)
            
            if isinstance(data, dict) and data.get('result', 'success') != 'success':
                raise PiwikError(data.get('message', 'Error occured during piwik call.'))
            
            return data
        return data
    
class PiwikError(Exception):
    pass
