# Glosary:
# mo: Match object
# regex: Regular Expresion abreviated


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


#^ $ vs \A \Z
# ^ and \A Ancors a match at the star of a string
# $ and \Z Ancors a match at the end of a string

text = "foobar"
regex = re.compile(r'foo\A', re.I)
mo = regex.search(text) #Returns foobar

# ^ and \A Ancors a match at the star of a string
text = "\nfoobar"
regex = re.compile(r'foo\A', re.I)
mo = regex.search(text) #Returns None because of the next line prior wich would work if 
# using ^

text = "foo\nbar\nbaz"
regex = re.compile(r'bar\Z', re.M) #to fix this we use re.Multiline(re.M shorten)
mo = regex.search(text)


text = "foo\nbar\nbaz"
regex = re.compile(r'bar\Z', re.M)
mo = regex.search(text)


# \B Anchosr a match to a location that is not a word boundry

regex = re.compile(r'\Bfoo\B')
mo = regex.search('barfoobaz')
print(mo)

# \b Anchosr a match to a word boundry
regex = re.compile(r'\bbar\b')
mo = regex.search('bar foo baz')
print(mo)

regex = re.compile(r'(bar)')
mo = regex.search('foo bar baz')
print(mo)

regex = re.compile(r'(bar)+')
mo = regex.search('foo barbarbar baz')
print(mo)

regex = re.compile(r'bar+')
mo = regex.search('foo barbarbar baz')
print(mo)

regex = re.compile(r'bar+')
mo = regex.search('foo barr baz')
print(mo)

regex = re.compile(r'(ba[rz]){2,4}(qux)?') #here we are stating that the permutation
#of bar or baz has to occur at list twice qux is optional
mo = regex.search('bazbarbazqux')
print(mo)
regex = re.compile(r'(ba[rz]){2,4}(qux)?')
mo = regex.search('barbazqux')
print(mo)

regex = re.compile(r'(ba[rz]){2,4}(qux)?')
mo = regex.search('barbaz')
print(mo)

regex = re.compile(r'(ba[rz]){1,4}(qux)?')#Here we modified to search for at least one
# permutation
mo = regex.search('bazqux')
print(mo)

# Group and Groups
regex = re.compile(r'(\w+),(\w+),(\w+)')
mo = regex.search('foo,qux,bar')
print(mo.groups()) #Here we are printin the tuple with al groups # type: ignore
print(mo.group(1)) #Here we are printin group 1# type: ignore
print(mo.group(2)) #Here we are printin group 2# type: ignore
print(mo.group(3)) #Here we are printin group 3# type: ignore
print(mo.group(2,3)) #Here we are printin groups 2 and3# type: ignore

# Back References
regex = re.compile(r'(\w+),\1') 
mo= regex.search('love,love')
print(mo) #Here we are referencing if the second group matches the first there for 
# we return love love

regex = re.compile(r'(\w+),\1')
mo= regex.search('love,like')
print(mo)#Here we are referencing if the second group matches the first there for 
# we return None

regex = re.compile(r'(\w+),\1')
mo= regex.search('like,like')
print(mo)#Here we are referencing if the second group matches the first there for 
# we return like like

regex = re.compile(r'([a-z])#\1')
mo= regex.search('a#a')
print(mo)#Here we are referencing if the second group matches the first there for 
# we return a#a

regex = re.compile(r'([a-z])#\1')
mo= regex.search('l#l')
print(mo)#Here we are referencing if the second group matches the first there for 
# we return l#l