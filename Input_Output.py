# Import string to check for punctuations
import string
def remove_punctuations(word):
    return "".join(i.lower() for i in word if i in string.ascii_letters)

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    text = remove_punctuations(text)
    return text == reverse(text)



something = input("Enter some words or text: ")
if is_palindrome(something):
    print("Yes,its palindrome")

else:
    print("No,it`s not a palindrome text")

