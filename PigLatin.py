# Instructions
# Like with any new language, it is crucial to learn the formal rules of pig Latin. This not only gives you a solid 
# foundation in the language game, but it also helps you understand its usage. These rules will also come handy if 
# you have a text to translate to pig Latin.

# Rules:
# 1. If Words Beginning With Consonants:
#   - Move first character from the initial location of that particular word to the last position of the name.
#   - Add a suffix the suffix “-ay” to the end of the word.
# 2. If Words Beginning With Vowels:
#   - Add a suffix the suffix “-yay” to the end of the word.
# Example1 
# Input: Alive*****Output1: Aliveyay
# Example2 
# Input: I love Python*****Output: Iyay ovelay Ythonpay
vowels = ('a','e','i','o','u')
def is_vowel(p_letter):
    for vowel in vowels:
        if p_letter == vowel or p_letter.lower() == vowel:
            return True
    return False
def firstLetterToLast(p_word):
    first_letter = p_word[0]
    p_word = p_word+first_letter
    return p_word[1:] 
sentence = input("Enter your text to convert to Pig Latin: ")
sentence = sentence.split()
new_sentence = []
index = 0
while index != len(sentence):
    word = sentence[index]
    if is_vowel(word[0]):
        word = word+"yay"
    else:
        word = firstLetterToLast(word)
        word = word+"ay"
    new_sentence.append(word)
    index += 1
new_sentence= " ".join(new_sentence)
print(new_sentence)
