from setuptools import setup, find_packages

setup(
    name='python-piwik-api',
    version='0.1',
    packages=find_packages(),
    py_modules= ['piwikapi',],
    install_requires=['requests', 'simplejson']
)
