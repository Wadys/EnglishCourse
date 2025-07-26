import re
# This prints ba plus any permutations onf letters
regex_object = re.compile(r'ba[artz]')
mo = regex_object.search('foorbarqux')
print(mo)

# This prints the first vowels found
vowel_regex = re.compile(r'[aeiou]')
mo = vowel_regex.search('foorbatqux')
print(mo)

# This prints the first lower case letter found
lowercase_regex = re.compile(r'[a-z]')
mo = lowercase_regex.search('QWEDADASsQWADASD')
print(mo)

# This prints all Upper case letter found
uppercase_regex = re.compile(r'[A-Z]')
mo = uppercase_regex.findall('QWEDADASsQWADASD')
print(mo)

# This prints all Upper and lower case letter found
letters_regex = re.compile(r'[a-zA-Z]')
mo = letters_regex.findall('QWED@A#D4A%Ss.QWADASD')
print(mo)

# This prints the all lowe case vowels found
vowel_regex = re.compile(r'[aeiou]')
mo = vowel_regex.findall('I Like to eat food outside')
print(mo)

# This prints the vowels found in both upper and lower cases
vowel_regex = re.compile(r'[aeiouAEIOU]')
mo = vowel_regex.findall('I Like to eat food outside')
print(mo)

# This prints double vowels found in both upper and lower cases
vowel_regex = re.compile(r'[aeiouAEIOU]{2}')
mo = vowel_regex.findall('I Like to eat food outside')
print(mo)

# This excludes vowels found in both upper and lower cases
consonant_regex = re.compile(r'[^[0-9]aeiouAEIOU]')
mo = consonant_regex.findall('I Like to eat food outside')
print(mo)
