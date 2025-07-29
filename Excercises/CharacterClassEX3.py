# Implement regular expression pattern inside a function to check that a string contains only
# a certain set of characters (in this case a-z, A-Z and 0-9).
# check_char("ABCDEFabef1250")
# check_char("*&%@#{")
# Output:
# ['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'e', 'f', '1', '2', '5', '0']
# []
import re
def check_char(text):
    rexgex = re.compile(r'[a-zA-z0-9]')
    mo = rexgex.findall(text)
    return mo
print(check_char('ABCDEFabef1250'))
print(check_char("*&%@#{"))