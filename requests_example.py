import requests
from bs4 import BeautifulSoup
webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/shellter.html', "html.parser")

soup = BeautifulSoup(webpage_response.content)
print(soup)