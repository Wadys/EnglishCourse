# ^ Character anchors a match at the start of a strig.
# $ Character anchors a match at the end of a string.
# . Character matches any single character except a newline.
# .* Uses a wild car to match any text in the string separated by space
import re
# ***Using ^
begin_hello_regex = re.compile(r'^Hello')
mo = begin_hello_regex.search("Hello there")
print(mo)
mo = begin_hello_regex.search("You said Hello there")
print(mo) #In this case 'None' is printer because the string doesn't start with Hello
begin_hello_regex = re.compile(r'world$')
mo = begin_hello_regex.search("Hello world.")
print(mo) #In this case 'None' is printer because the string doesn't end with 'world'
mo = begin_hello_regex.search("Hello world")
print(mo) 

# ***Using $
all_digits_regex = re.compile(r'^\d+')
mo = all_digits_regex.search('473846583984848484848') 
print(mo) 
all_digits_regex = re.compile(r'^\d+')
mo = all_digits_regex.search('47384658X3984848484848')
print(mo) #In this case only 8 digits are pulled because there is an ex in the middle
all_digits_regex = re.compile(r'^\d+$')
mo = all_digits_regex.search('473846583984848484848')
print(mo) #In this case all digits are pulled because the numer start and cuntinues 
# ending in digites
all_digits_regex = re.compile(r'^\d+$')
mo = all_digits_regex.search('47384658x3984848484848')
print(mo) #In this case 'None' is printed beacaus there is not match for a number that starts
# in digits continiusly ending in digits(There is an x in the middle)

# ***Using .
regex = re.compile(r'.ad')
mo = regex.findall("The love you donwload still is equal to the love you upload")
print(mo)#Here we print both times the ad is bieng shown in the string and the character 
# before it in bothcases 'o'

regex = re.compile(r'.{1,5}ad')
mo = regex.findall("The love you donwload still is equal to the love you upload")
print(mo)#Here we print five characters prior to ad
regex = re.compile(r'.{1,7}ad')
mo = regex.findall("The love you donwload still is equal to the love you upload")
print(mo)#Here we print the 7 characters prior to ad in both cases the spaces are ccounted as 
# characters even though they are in diferent places

# ***Using .*
text = "Make: BMW Model: X5"
car_regex = re.compile(r'Make: (.*) Model: (.*)')
mo = car_regex.findall(text)
print(mo)#Here we print the list with bith element

# ***Using .* greedy vs non greedy
# Greedy
text = "<Hello world> Welcome!>"
regex = re.compile(r'<(.*)>')
mo = regex.search(text)
print(mo)#Here we return the whole text between the '<' and the last '>' 

# Non Greedy
text = "<Hello world> Welcome!>"
regex = re.compile(r'<(.*?)>')
mo = regex.search(text)
print(mo)#Here we return the whole text between the '<' and the first '>'

# ***Using .* new line
new_text = "I love Python.\n I enjoy learning it using online Python for Everyone course"
print(new_text)
regex = re.compile(r'.*')
mo = regex.search(new_text)
print(mo)#Here we return the text up to the new line break'>' 

regex = re.compile(r'.*', re.DOTALL)
mo = regex.search(new_text)
print(mo)#Here we return the whole text'>'

vowel_regex = re.compile(r'[aeiou]') 
mo = vowel_regex.findall('I love Python')# Same as before I is being ignores for being 
# in upper case
print(mo)

vowel_regex = re.compile(r'[aeiou]', re.IGNORECASE) # Same as re.IGNORECASE Ignores upper cases
mo = vowel_regex.findall('I love Python')
print(mo)
