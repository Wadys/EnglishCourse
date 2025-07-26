# Greedy Operators are going to return the maximum ammount of characters posible in the text
import re

#Greedy Operators return count of 4 because it's the maximum amount of 'a's in the text
print("***Greedy Operators")
regex = re.compile('a*')
mo = regex.search('aaaa') 
print(mo) 

regex = re.compile('a+')
mo = regex.search('aaaa')
print(mo) 

regex = re.compile('a{0,4}')
mo = regex.search('aaaa')
print(mo)

# Not Geedy Operators return count of 1 because it's the minimum amount of 'a's in the text
# The only exption is the ? operator becaus the minimum is none at all
# Not Geedy Operators are the same but with a question mark(?) at the end 

print("***Not Greedy Operators")
regex = re.compile('a?')
mo = regex.search('aaaa')
print(mo)


regex = re.compile('a*?')
mo = regex.search('aaaa')
print(mo)

regex = re.compile('a+?')
mo = regex.search('aaaa')
print(mo)

regex = re.compile('a{1,4}?')
mo = regex.search('aaaa')
print(mo)

#None greedy runs performance fasteser than greedy
#When using the searchall the greedy approache will be faster performance wise

