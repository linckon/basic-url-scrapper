import re
import requests

target_url = 'https://books.toscrape.com/'
response = requests.get(target_url)
url_pattern = re.compile('<a href="(.*?)">')
result = url_pattern.findall(response.text)
print(result)

with open('urls.txt','w') as f:
    f.write('\n'.join(result))