#Step 1 - Create sentece maker function
#Step 2 - Create a loop which asks input from user continiously
#Step 3 - Combine everything
from os import system as s
def sentence_creator(text):
    list_words = ['what', 'how', 'where', 'why', 'who']
    for word in list_words:
        if text.startswith(word) or text.startswith(word.capitalize()):
            return text.capitalize() + '?'
    return text.capitalize() + '.'                                          
# My solution using strings should have used lists
# def text_creator():
#     story = ''
#     while True:
#         text = input("What's on your mind? ")
#         if text == '\\end':
#             return story
#         else:
#             story += sentence_creator(text) + ' '
def text_creator():
    result = []
    while True:
        text = input("What's on your mind? ")
        if text == '\\end':
            break
        else:
            complete_sentence = sentence_creator(text)
            result.append(complete_sentence)
    story = " ".join(result)
    return(story)
s('cls')
print(text_creator())