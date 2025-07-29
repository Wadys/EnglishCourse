# Instructions:
# Write a Python function to extact the email addresses from the given string.

# text = """From test@appmillers.com Wen Jan  5 09:14:16 2022\nFrom info@appmillers.com
# Wen Jan  5 09:14:16 2022\nFrom elshad@appmillers.com Wen Jan  5 \nFrom 
# redy@appmillers.com Wen Jan  5 \nFrom info@appmillers.com Wen Jan  5 """

# Example Input:
# extract_email(text)

# Example Output:
# ['test@appmillers.com', 'info@appmillers.com', 'elshad@appmillers.com', 
# 'redy@appmillers.com', 'info@appmillers.com']

import re
text = """From test@appmillers.com Wen Jan  5 09:14:16 2022\nFrom info@appmillers.com
Wen Jan  5 09:14:16 2022\nFrom elshad@appmillers.com Wen Jan  5 \n
From redy@appmillers.com Wen Jan  5 \nFrom info@appmillers.com Wen Jan  5 """

def extract_email(text):
    regex_email = re.compile(r"[a-zA-Z]+@[a-zA-Z]+.com")
    mo = regex_email.findall(text)
    return mo

def extract_email_improved(text):
    regex_email = re.compile(r"\w+@\w+.com")
    mo = regex_email.findall(text)
    return mo

print(extract_email(text))