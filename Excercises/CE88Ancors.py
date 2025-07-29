
#Istructions:
#Implement a Python function which takes text as a parameter and return the list 
#of words which are three, four or five characters long.

#Example:
#find_words("I like Python for Everyone course. It is the best one out there.")

# Output:
# ['like', 'for', 'the', 'best', 'one', 'out', 'there']

import re
def find_words(text):
    regex_text = re.compile(r'\b\w{3,5}\b')
    text_list = text.split()
    return_list = []
    for i in text_list:
        mo = regex_text.findall(i)
        return_list.extend(mo)
    return return_list
print(find_words("I like Python for Everyone course. It is the best one out there."))