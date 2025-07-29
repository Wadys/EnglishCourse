# Replaces the dots for exlamation marks 
text = "d.o.g."
text2 = text.replace('.','!')
print(text2)

#This finds the position where a character begius
data = 'From example.email@efu.co.uk Sat Sep 5 09:14:16 2021'
at_index = data.find("@")
print(at_index)

#In this case it takes the position and can find the domain
space_after_at = data.find(" ", at_index)
domain = data[at_index : space_after_at]
print(domain)

#Here you can take a string and split it
my_string = "I love learning Python"
output = my_string.split()
print(output)

#Here you can take a string and split it by dashes as separators 
my_string = "I-love-learning-Python"
output = my_string.split("-")
print(output)

#Here you can take a string and split it by dashes as separators and split its as two 
# words whats infront of the dash and the rest of the string
my_string = "I-love-learning-Python"
output = my_string.split("-", maxsplit=2)
print(output)

#You a can also reconstruct the text and us a separate character as a separator
my_string = "I-love-learning-Python"
output = my_string.split("-")
print(output)
join_back = "/".join(output)
print(join_back)