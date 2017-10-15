# Caeser Cypher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

message = input("Text to be encrypted: ")
inputString = message.lower()
shift = int(input("No. of places to be shifted: "))


translated_msg = {}

for i in range(0, 26):
    letter = alphabet[i]
    translated_msg[letter] = alphabet[(i+shift)%26]
    print(alphabet[i] + ":" + translated_msg[letter])

cypherText = ''

for letter in inputString:
    if letter in translated_msg:
        letter = translated_msg[letter]
        cypherText = cypherText + letter
    else:
        cypherText = cypherText + ' '

print(cypherText)
