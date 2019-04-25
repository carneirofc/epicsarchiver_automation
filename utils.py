import os
import sys
import logging
import requests

def login(username, password, url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {'username':username, 'password':password}

    session = requests.Session()
    response = session.post(url + '/login', headers=headers, data=payload, verify=False)
    return session if b'authenticated' in response.content else None


def configureLogging(verbose):
    root = logging.getLogger()
    root.setLevel(logging.DEBUG if verbose else logging.INFO)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)
    #import http.client as http_client
    #http_client.HTTPConnection.debuglevel = 1
