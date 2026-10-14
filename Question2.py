
s="programming"
char_count = {}
for char in s:
    # if char in char_count:
    #     char_count[char] += 1
    # else:
    #     char_count[char] = 1
    char_count.get(char, 0)
print("Character Occurrences in the string:", char_count)