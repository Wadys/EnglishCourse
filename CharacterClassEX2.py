#Implement a function which extracts year, month and date from an url by using regular 
# expression pattern.
# url = https://www.apmillers.com/news/daily/wp/2022/02/02/regular-expressions-patterns/
# extract_date(url)
# Output
# [('2022', '02', '2')]
import re
url = '''https://www.apmillers.com/news/daily/wp/2022/02/02/regular-expressions-patterns/'''

def extract_date(url):
    regex = re.compile(r'(\d{4})/(\d{1,2})/(\d){1,2}')
    mo = regex.findall(url)
    return mo
print(extract_date(url))