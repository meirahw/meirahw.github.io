from bs4 import BeautifulSoup
import time
import requests

def urlRequestTable(url, url_type):
    
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('a', href = lambda s: s.startswith(url_type))

    time.sleep(2)
    
    return table

def urlRequestSoup(url):
    
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    time.sleep(2)

    return soup