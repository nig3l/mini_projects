# from bs4 import BeautifulSoup
# import requests

# response = requests.get("https://www.britannica.com")

# soup = BeautifulSoup(response.content,'html.parser')

# # print(soup.find_all('h1'))

# # finding all the links
# for link in soup.find_all('a'): 
#     print(link.get('href'))

import requests
URL = "https://www.geeksforgeeks.org/data-structures/"
r = requests.get(URL)
print(r.content)
