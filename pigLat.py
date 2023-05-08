# English to Pig Latin
print('Enter the english message to translate into Pig Latin:')
message = input()
VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = [] # A list of the words in Pig Latin
for  word in message.split():
    #Separate the non-letter at the start of this word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
       prefixNonLetters += word[0]
       word = word[1:]

    if len(word) == 0:
       pigLatin.append(prefixNonLetters)
       continue

    #Separate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
       suffixNonLetters += word[-1]
       word = word[:-1]

    # Remember if the word was in uppercase or title cse
    wasUpper = word.isupper()
    wasTittle = word.title()

    word = word.lower() # make the word lowercase for translation

    #separe the consonats at the start of this word
    prefixConsonats = ''
    while len(word) > 0 and not word[0] in VOWELS:
       prefixConsonats += word[0]
       word = word[1:]

    # Add the pig latin ending to the word:
    if prefixConsonats != '':
       word += prefixConsonats + 'ay'
    else:
       word += 'yay'

    # set the word back to uppercse or title case:
    if wasUpper:
       word = word.upper()
    if wasTittle:
       word = word.title()

    # Add the non-letters back to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# Join all the words back together into a single string:
print(' '.join(pigLatin))