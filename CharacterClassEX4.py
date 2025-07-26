# Write a Python function to find all character combinations starting with 'a' or 'e' in a 
# given string.

# Example:
# text = "The following example creates a list with 50 elements. 
# All elements are then added to the list when the list is created."
# start_ae(text)

# Output:
# ['example', 'eates', 'elements', 'elements', 'are', 'en', 'added', 'en', 'eated']
import re
def start_ae(text):
    regex_ae = re.compile(r'([ae]\w+)')
    mo = regex_ae.findall(text)
    return mo

text = "The following example creates a list with 50 elements. All elements are then added to the list when the list is created."
print(start_ae(text))
