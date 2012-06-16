Python PiwikAPI
================

This API is a wrapper around Piwik REST interface. By calling api methods, http 
requests are created dynamically.

For all methods see http://piwik.org/docs/analytics-api/reference/


## Usage 
Just append full method name with parameters after PiwikAPI object.

```python
PIWIK_URL = 'http://demo.piwik.org/'
PIWIK_TOKEN = '53983b97138c69b72b0a32bbfeedc213'

from piwikapi import PiwikAPI

piwik = PiwikAPI(PIWIK_URL, PIWIK_TOKEN)
piwik.SitesManager.getAllSites()
piwik.UsersManager.getUser(userLogin='tomas4')
```

## Installation
$ pip install git+git://github.com/tomasd/python-piwik-api.git