# \d Any number from 0 to 0.
# \D Any Charactter tha s not a numeric digit from 0 to 9.
# \w Any letter, numeric digit or the underscore(_) character.
# \W Any character that is not a letter, numeric digit or the underscore(_) character.
# \s Any space, tab or newline character.
# \S Any character that is not a space, tab or newline character.

import re

# Here we are looking for the first digits from 0 to 9 but putting one by one the digits
phone_regex = re.compile(r'(0|1|2|3|4|5|6|7|8|9)')
mo = phone_regex.search('555-666-8888')
print(mo)
# Here we are looking for digits from 0 to 9 that follow the phone format
phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_regex.search('555-666-8888')
print(mo)

# Here we are looking for the first digits using \d
phone_regex = re.compile(r'\d')
mo = phone_regex.search('asd5uio')
print(mo)

# Here we are looking for the first character that is not a digits using \D
phone_regex = re.compile(r'\D')
mo = phone_regex.search('asd5uio')
print(mo)

# Here we are looking for the first character that is a digits, letter or undersscoreusing \w
phone_regex = re.compile(r'\w')
mo = phone_regex.search('@#$%>/.w_(*@#&)')
print(mo)

# Here we are looking for all characters that are digits, letter or undersscoreusing \w
phone_regex = re.compile(r'\w')
mo = phone_regex.findall('@#$a%1>/.w_(*@#d&)')
print(mo)

# Here we are looking for all characters that are digits, letter or undersscoreusing \w
phone_regex = re.compile(r'\W')
mo = phone_regex.findall('@#$a%1>/.w_(*@#d&)')
print(mo)

# Here we are looking for the firs characters that is spaces tab or newline \w
phone_regex = re.compile(r'\s')
mo = phone_regex.search('foo bar\n\t')
print(mo)

# Here we are looking for all characters that are spaces tab or newline \w
phone_regex = re.compile(r'\s')
mo = phone_regex.findall('foo  bar\n\t')
print(mo)

# Here we are looking for all characters that are not spaces tab or newline \w
phone_regex = re.compile(r'\S')
mo = phone_regex.findall('foo  bar\n\t')
print(mo)

# Applicable example:
text = '''The use of 1234 to say "I Love You" comes from the following idea:
I have 1 thing 2 say: 3 words 4 you'''

regex = re.compile(r'\d+\s\w+')
mo = regex.findall(text)
print(mo)
