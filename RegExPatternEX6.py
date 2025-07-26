# Write a Python function to find sequences of capital letters joined with an underscore. 
# If match is found it returns Matched otherwise Not matched.

# Example:
# text_match("BB_CCAA")
# text_match("aabb_DDDEFF")
# text_match("ADRGT_BCDEe")

# Output:
# Matched
# Not matched
# Not matched

import re
def text_match(text):
    regex = re.compile(r'^([A-Z]+_[A-Z]+$)')
    mo = regex.search(text)
    # return mo
    if mo == None:
        return "Not matched"
    else:
        return "Matched"
    
print(text_match("BB_CCAA"))
print(text_match("aabb_DDDEFF"))
print(text_match("ADRGT_BCDEe"))