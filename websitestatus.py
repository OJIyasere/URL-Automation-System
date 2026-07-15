'''This is just to check if there are other website statuses 
other than 200 that mean the website is working'''

import requests 
from bs4 import BeautifulSoup

url = input("Enter URL: ")
response = requests.get(url) 


statusCode = response.status_code
print(f"Website Status: {statusCode}")
