# Instructions:
# Write a Python function to match a string that has a 'c' or 'C' followed by 
# anything, ending in 'e' or 'E'. If match is found it will return the list of matches.

#Input:
# text = 'I come to CTRE every year'
# text_match(text)
#Output:
# ['come', 'CTRE']

import re
text = 'I come to CTRE every year'
def text_match(text):
    regex_text_match = re.compile(r'c.\w+e$' ,re.IGNORECASE)
    text_list = text.split()
    result = []
    for i in text_list:
        mo = regex_text_match.findall(i)
        result.extend(mo)
    return result

print(text_match(text))

