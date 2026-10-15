s="Python 123"
vowels="aeiouAEIOU"
vowel,consonant,space,digit=0,0,0,0
for i in s:
    if i.isdigit():
        digit+=1
    elif i.isspace():
        space+=1    
    elif i in vowels:
        vowel+=1
    else:
        consonant+=1    
print("Vowels:",vowel)
print("Consonants:",consonant)
print("Spaces:",space)
print("Digits:",digit)