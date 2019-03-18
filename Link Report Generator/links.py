import requests
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from urllib.error import URLError
import pandas as pd
import argparse
from urllib.request import urlopen, Request

parser = argparse.ArgumentParser(description='Enter a url')
parser.add_argument('url', help="Enter a url")
args = parser.parse_args()

url = args.url
session = requests.Session()


header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
          "Accept-Language": "en-US,en;q=0.5",
          "Connection": "keep-alive",
          "Referrer": "https://www.google.com/",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}


base = urlparse(url).netloc
page = session.get(url, headers=header).text
cursor = BeautifulSoup(page)

internal_links = []
external_links = []

total = len(cursor.findAll('a'))
for i in cursor.findAll('a'):
    try:
        l = i.attrs['href']
        if l:
            if l.startswith('#'):
                pass
            elif l.startswith('/'):
                l = urljoin('http://'+base+'/', l[1:])
                internal_links.append(l)
            elif l.startswith('../'):
                l = urljoin('http://'+base+'/', l[3:])
                internal_links.append(l)
            else:
                external_links.append(l)
    except KeyError:
        pass

response = {}
for i in internal_links:
    try:
        request = Request(url=i, headers=header)
        code = urlopen(request).getcode()
        print('Checking {} -- Status : {}'.format(i,
                                                  code))
        # status_code = urllib.request.urlopen(i).getcode()
        response[i] = code
    except TimeoutError:
        response[i] = 'timeout'
        print('Timeout')
    except urllib.error.URLError as e:
        response[i] = e.reason
        print(e.reason)
    except urllib.error.HTTPError as e:
        response[i] = e.code
        print(e.code)
    except Exception as e:
        response[i] = e
        print('An exception occured')

response_ext = {}
for i in external_links:
    try:
        request = Request(url=i, headers=header)
        code = urlopen(request).getcode()
        print('Checking {} -- Status : {}'.format(i, code))
        # status_code = urllib.request.urlopen(i).getcode()
        response_ext[i] = code
    except TimeoutError:
        response_ext[i] = 'Timeout'
        print('Timeout')
    except urllib.error.URLError as e:
        response_ext[i] = e.reason
        print(e.reason)
    except urllib.error.HTTPError as e:
        response_ext[i] = e.code
        print(e.code)
    except Exception as e:
        response_ext[i] = e
        print('An exception occured')


series_int = pd.Series(response, name='Response')
series_int.index.name = 'URL'
df1 = pd.DataFrame(series_int)
df1['Type'] = 'Internal'

series_ext = pd.Series(response_ext, name='Response')
series_ext.index.name = 'URL'
df2 = pd.DataFrame(series_ext)
df2['Type'] = 'External'

results = pd.concat([df1, df2])
results.to_csv('report.csv')

print(results)
