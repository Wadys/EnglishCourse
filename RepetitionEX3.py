
# Write a Python function that matches given words in the text and count them.
# Words: Love, love, Lovers, lovers
# Text: Lovers in love
      # Lovers in love
      # Love, love, love, love, love
      # Love, love, love, love, love
      # Love, love, love, love, love
      # Love, love, love, love, love
      # Lovers loving love just like these lovers are loving love in love
      # Lovers loving love just like these lovers are loving love in love

# Input:
    # text_match(text)
# Output:
    # 34
import re
text = '''Lovers in love
Lovers in love
Love, love, love, love, love
Love, love, love, love, love
Love, love, love, love, love
Love, love, love, love, love
Lovers loving love just like these lovers are loving love in love
Lovers loving love just like these lovers are loving love in love'''
def text_match(text):
    # Long Solution
        # regex = re.compile(r'(L|l)ove(rs)?')
        # list_text = text.split()
        # count = 0
        # for word in list_text:
        #     mo = regex.search(word)
        #     if mo != None:
        #         count += 1
        # return count
    # Short Solution
        regex = re.compile(r'(L|l)ove(rs)?')
        mo_list = regex.findall(text)
        return len(mo_list)
print(text_match(text))