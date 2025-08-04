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
# RegEx Flags:
# re.I  re.IGNORECASE   -Makes matchin of alphabetic characters case-insensitive
# re.M  re.MULTILINE    -Causesstart og string an end of string anchors to match 
#                       embedded newlines
# re.S  re.DOTALL       -Causes the dot metacharacter to match a new line
# re.X  re.VERVOSE      -Allows inclusion of whitespace and comments within a 
#                       regular expression
# -     re.DEBUG        -Causes the regex parser to display debugging information 
#                       to the console
# re.A  re.ASCII        -Specifies ASCII encoding for character clasiffication
# re.U  re.UNICODE      -Specifies Unicode encoding for character clasiffication

# re.I  re.IGNORECASE
# The following examples do the same, look for a characters
regex = re.compile(r'a+',re.IGNORECASE) 
mo = regex.search('aaaaAAAA')
print(mo)

mo = re.search(r'a+','aaaaAAAA',re.IGNORECASE)
print(mo)

mo = re.search(r'a+','aaaaAAAA',re.I)
print(mo)

# re.M  re.MULTILINE
custom_string = 'foo\nbar\nbaz'
mo = re.search(r'foo', custom_string)
print(mo) #Here foo is found at the start of the strng

custom_string = 'foo\nbar\nbaz'
mo = re.search(r'foo$', custom_string)
print(mo) #Here None is returned because fooo is not at the end

custom_string = 'foo\nbar\nbaz'
mo = re.search(r'foo$', custom_string, re.MULTILINE)
print(mo) #Here since we are looking for foo in multiple lines

custom_string = 'foo\nbar\nbaz'
mo = re.search(r'foo$', custom_string, re.M)
print(mo) #Here since we are looking for foo in multiple lines

# re.S  re.DOTALL
custom_string = 'foo\nbar'
mo = re.search(r'foo.bar', custom_string)
print(mo) #Here the period is not recogniced and None is returned

custom_string = 'foo\nbar'
mo = re.search(r'foo.bar', custom_string, re.DOTALL)
print(mo) #Here the period is reconiced as a new line there for the foo\nbar is returned

custom_string = 'foo\nbar'
mo = re.search(r'foo.bar', custom_string, re.S)
print(mo) #Here the period is reconiced as a new line there for the foo\nbar is returned

# re.X  re.VERVOSE
regex_phone = r'''
        ^                       # Start of string
        (\(\d{3}\))?            # Optional area Code
            \s*                 # Optional whitespace
            \d{3}               # Three digit prefix
            [-.]                # Separator character
            \d{4}               # Four digit line number
            $                   # Anchor for end of string
            '''
mo = re.search(regex_phone, '(123) 313-7878', re.VERBOSE)
print(mo)

# Searching funcions:
# re.search:    Scan through string looking for a match to the pattern
# re.match:     Matches pattern at the start of the string
# re.fullmatch: Matches pattern in the entrie string
# re.findall:   Returns a list of all regular expresion matching in a string
# re.finditer:  Return an iterator over all non-overlapping matches in the string

# Search:
mo = re.search(r'[a-z]+', 'foo123BAZ')
print(mo)

mo = re.search(r'[a-z]+', 'FOO123BAZ', re.I)
print(mo)

mo = re.search(r'[a-z]+', 'FOO123BAZ')
print(mo) 

# Match:
mo = re.match(r'[A-Z]+', 'FOO123BAZ')
print(mo) #String starts with capital letters
mo = re.match(r'\d+', 'FOO123BAZ') 
print(mo) #String does not starts with digits there for None is returned 

#Fullmatch:
mo = re.search(r'\d+', '123test')
print(mo) #String findes and returns 123 
#Vs
mo = re.fullmatch(r'\d+', '123test')
print(mo) #Returns None because it needs to meet the full criteria

mo = re.fullmatch(r'\d+', '123523242')
print(mo) #The full criteria is met so rturns the value
mo = re.fullmatch(r'\w+', 'aqqdsdfsdsfdiugsduf')
print(mo) #The full criteria is met so rturns the value

#Findall:
mo = re.findall(r'(\w+)', ',,..1235...23242...foo...bar....baz')
print(mo) #Once the criteria is met the matches are added to a list

#Finditer:
for i in re.finditer(r'(\w+)', ',,..1235...23242...foo...bar....baz'):
    print(i) #Return the iterable of the objet fund

#Substitution Functions:
#re.sub():      Scans a string for regex matches, replaces the matching portion of 
#               the string with the specified replacement strig, and returns the result
# re subn():    Behaves just like re.sub() but also returns information regarding 
#               the number of substitutions made
custom_text = '123.foo..456,bar-789.baz'
result_string = re.sub(r'\d+','#',custom_text)#Replaces digits with #
print(result_string)
result_string = re.sub(r'[a-z]+','*',custom_text)#Replaces letters with *
print(result_string)
print(custom_text)
result_string = re.sub(r'123.(\w+)\..456\,bar-789\.(\w+)',r'123.\2..456,bar-789.\1',custom_text)
#Replaces the order of the strings switching the foo and the baz
print(result_string)

result_string = re.sub(r'123.(\w+)\..456\,bar-789\.(\w+)',
                       r'123.\2..456,bar-789.\1',
                       custom_text) #This is a more readable way to view it
print('Readable view: '+result_string)

result_string = re.sub(r'123.(?P<w1>\w+)\..456\,bar-789\.(?P<w2>\w+)',
                       r'123.\g<w2>..456,bar-789.\g<w1>',
                       custom_text) #In here we are using group names
print('Group Name:    '+result_string)
result_string = re.sub(r'123.(?P<w1>\w+)\..456\,bar-789\.(?P<w2>\w+)',
                       r'123.\g<2>..456,bar-789.\g<1>',
                       custom_text) #In here we are using group number
print('Group Number:  '+result_string)
# Ex: Add 0 at the end of every digit
custom_string = 'foo 123 bar'
result_string = re.sub(r'(\d+)', r'\g<1>0', custom_string)
print(result_string)

def f(match_obj):
    s = match_obj.group(0)
    if s.isdigit():
        return str(int(s) * 10)
    else:
        return s.upper()
mo = re.sub(r'\w+', f, 'foo.bar.10.baz.20')
print(mo)# Here we use the F function to be executed for every matching criteria

mo = re.sub(r'\w+', 'xxx', 'foo.bar.qux.baz', count=2)
print(mo)#Here we are changing the xxx for the first two matching groups

mo = re.sub(r'\w+', 'xxx', 'foo.bar.qux.baz', count=3)
print(mo)#Here we are changing the xxx for the first three matching groups

mo = re.subn(r'\w+', 'xxx', 'foo.bar.qux.baz', count=3)
print(mo)#Subn returns a tuple with the changes and the number of groups impacted

mo = re.subn(r'\w+', f, 'foo.bar.10.baz.20')
print(mo)#Subn returns a tuple with the changes and the number of groups impacted by f


#Utility Functions:
# re.split():    Splits a string into substring usisg a regex as a delimiter
# re.escape():   Escape characters ina a regex


# re.split():
result = re.split('s*[,;/]\s*','foo,bar ; test / python') # type: ignore
print(result)#We are spliting a string removing comas, slashes and semicolons

result = re.split('(s*[,;/]\s*)','foo,bar ; test / python') # type: ignore
print(result)#We are spliting in groups the different elements

regex = r'(s*[,;/]\s*)'
result = re.split(regex,'foo,bar ; test / python')
for i,s in enumerate(result):
    if not re.fullmatch(regex, s):
        result[i] = f'<{s}>'
print(result)#We are spliting in groups the different elements and adding < > for the text ones

regex = r'(s*[,;/]\s*)'
result = re.split(regex,'foo,bar ; test / python')
for i,s in enumerate(result):
    if not re.fullmatch(regex, s):
        result[i] = f'<{s}>'
result= ''.join(result)
print(result)#We are spliting in groups the different elements and adding < > for the 
             #text ones adn returing it as a string

regex = r'(s*[,;/]\s*)'
result = re.split(regex,'foo,bar ; test / python')
print(result) #Capturing all including the delemeters

regex = r'(?:s*[,;/]\s*)'
result = re.split(regex,'foo,bar ; test / python')
print(result)#Capturing all without the delimiters

regex = r'(?:s*[,;/]\s*)'
result = re.split(regex,'foo,bar ; test / python',maxsplit=1)
print(result)#Captures one parameter and the rest is entred in one string

regex = r'(?:s*[,;/]\s*)'
result = re.split(regex,'foo,bar ; test / python',maxsplit=2)
print(result)#Captures two parameter and the rest is entred in one string

regex = r'(?:s*[,;/]\s*)'
result = re.split(regex,'foo,bar ; test / python',maxsplit=3)
print(result)#Captures three parameter and the rest is entred in one string

#re.escape
regex = r'foo^bar(baz)|qux'
result = re.match(regex, 'foo^bar(baz)|qux')
print(result)#Doesn't match

regex = r'foo\^bar\(baz\)\|qux'
result = re.match(regex, 'foo^bar(baz)|qux')
print(result) #Needs the \ in all text to match

regex = r'foo^bar(baz)|qux'
result = re.match(re.escape(regex), 'foo^bar(baz)|qux')
print(result) #The escape functions removes the need for the \ characters


