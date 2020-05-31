import requests
import re
from bs4 import BeautifulSoup

# the whole thing is a mess and is just for examples

def has_shellter_text(tag):
    return tag.string == "The Shellter"


webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

counter = 0

print("Line " + str(counter))
counter+=1

print(soup.p)
print("Line " + str(counter))
counter+=1

print(soup.p.string)
print("Line " + str(counter))
counter+=1

for children in soup.div:
    print("Line " + str(counter))
    counter+=1
    print(children)

print("Line " + str(counter))
counter+=1

turtle_links = soup.find_all('a')

print(turtle_links)
print("Line " + str(counter))
counter+=1

all_ul_li = soup.find_all(re.compile("[ou]l"))

print(all_ul_li)
print("Line " + str(counter))
counter+=1

all_h1_h9 = soup.find_all(re.compile("h[1-9]"))

print(all_h1_h9)
print("Line " + str(counter))
counter+=1

all_h1_a_p = soup.find_all(['h1', 'a', 'p'])

print(all_h1_a_p)
print("Line " + str(counter))
counter+=1

all_class_banner = soup.find_all(attrs={'class':'banner'})

print(all_class_banner)
print("Line " + str(counter))
counter+=1

all_class_banner_id_jumbotron = soup.find_all(attrs={'class':'banner', 'id':'jumbotron'})

print(all_class_banner_id_jumbotron)
print("Line " + str(counter))
counter+=1


# call our function 
shelter_text_elems = soup.find_all(has_shellter_text)

print(shelter_text_elems)
print("Line " + str(counter))
counter+=1


