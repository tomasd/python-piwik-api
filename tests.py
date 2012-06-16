from unittest.case import TestCase
from piwikapi import PiwikAPI
import requests
from requests.models import Response

class PiwikTest(TestCase):
    def testCreateUrl(self):
        def _mock_get(url, **kwargs):
            self.assertEquals('http://demo.piwik.org/', url)
            self.assertEquals({'module' : 'API',
                'method' : 'Referers.getKeywords',
                'format' : 'json',
                'idSite':3,
                'date':'yesterday',
                'period':'day',
                'token_auth':'1231',
                'filter_limit':10}, kwargs.get('params'))
            return response
            
        response = Response()
        response.status_code = 200
        response._content = '{"result":"success", "xxx":"aaa"}'
        old_get = requests.get
        
        try:
            requests.get = _mock_get
            
            api = PiwikAPI('http://demo.piwik.org/', '1231')
            self.assertEquals({"result":"success", "xxx":"aaa"},
                               api.Referers.getKeywords(idSite=3,
                                                        date='yesterday',
                                                        period='day',
                                                        filter_limit=10))
        finally:
            requests.get = old_get
