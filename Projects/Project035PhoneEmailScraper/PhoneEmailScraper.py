# Instructions
# Write a Python script which extracts every single phone number and email from
# data.py file text.

# TODOs:
# TODO 1 - Create Regex for Phone number
#     - Area code (optional)
#     - First Separator
#     - First three digits
#     - Separator
#     - Last 4 digits
#     - Extension (optional)    
# TODO 2 - Create Regex for Email
#     - Name part (including .+_)
#     - @ symbol
#     - Domain name part
# TODO 3 - Extract phone number/email from text
# TODO 4 - Print phone numbers and emails each on new line.
import re
from data import text
# TODO 1 - Create Regex for Phone number
#     - Area code (optional)
#     - First Separator
#     - First three digits
#     - Separator
#     - Last 4 digits
#     - Extension (optional)
phone_regex = re.compile(r'''(
                        ((\d\d\d)|(\(\d\d\d\)))?    # Area code optional
                        (\s|-)?                     # First separator
                        \d\d\d                      # First three digits
                        -                           # Separator
                        \d\d\d\d                    # Last Four Digits
                        (\s((ext(\.)?\s)|x)(\d{2,5}))?
                        )
                        ''', re.VERBOSE)

# TODO 2 - Create Regex for Email
#     - Name part (including .+_)
#     - @ symbol
#     - Domain name part
email_regex = re.compile('''
                        [a-zA-Z0-9_.+]+     #Name part
                        @                   #@ symbol
                        [a-zA-Z0-9_.+]+     #Domain part
                        ''', re.VERBOSE)
# TODO 3 - Extract phone number/email from text

extracted_pone_number = phone_regex.findall(text)
all_phone_numbers = []
for phone_number in extracted_pone_number:
    all_phone_numbers.append(phone_number[0])
extracted__emails = email_regex.findall(text)

# TODO 4 - Print phone numbers and emails each on new line.
results = '\n'.join(all_phone_numbers) + '\n'.join(extracted__emails)
print(results)