## Decoding the cypher using BruteForce Attack

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

inputString = input("Text to be decrypted: ")
inputString = inputString.lower()

translated_msg = {}

def createDict(shift):
    for i in range(0, 26):
        letter = alphabet[i]
        translated_msg[letter] = alphabet[(i+shift)%26]

def deCode(message):
    cypherText = ''
    for letter in message:
        if letter in translated_msg:
            letter = translated_msg[letter]
            cypherText = cypherText + letter
        else:
            cypherText = cypherText + ' '
    print(cypherText)

for i in range(0, 26):
    createDict(i)
    deCode(inputString)


