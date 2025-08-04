#Instruction:
# Implement a Python function which takes as a parameter IP address, removes leading 
# zeros from it and returns it.
# Example: remove_zero("211.07.095.122")
# Output: 211.7.95.122
import re

def remove_zero(ip_address):
    mo = re.sub(r'0','',ip_address)
    return mo

print(remove_zero('211.007.095.122'))