Stanza = "Baa, baa, black sheep,\"" \
         "Have you any wool?\""\
         "Yes, sir, yes, sir,\"" \
         "Three bags full;\n"
vowel = []
otherLetters = []
for letter in Stanza:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        vowel.append(letter)
    else:
        otherLetters.append(letter)

print("Total vowels in Stanza are ", len(vowel), vowel)
print("Total Alphabets except vowels in Stanza are ", len(otherLetters), otherLetters)

