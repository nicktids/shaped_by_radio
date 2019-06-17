import requests
import urllib
import json
import lxml.html
from lxml import etree

from bs4 import BeautifulSoup

url = 'http://www.bbc.co.uk/programmes/'
end ='b09y1xkp'


MAH = 'https://www.bbc.co.uk/programmes/b01pp0xq/episodes/player'

import logging

# These two lines enable debugging at httplib level (requests->urllib3->http.client)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


url_get = url + end
url_get_segments = url_get + '/segments.inc'
url_get_segments_json = url_get + '/segments.json'

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'})
html = session.get(url_get)
seg1 = session.get(url_get_segments)

sessionCookies = html.cookies

seg_json = session.get(url_get_segments_json, cookies = sessionCookies)

