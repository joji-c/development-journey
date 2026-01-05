def consonent_count(word):
    VOWELS = "aeiou"
    c_count=0
    for ch in word.casefold():
        if ch not in VOWELS and ch.isalpha():     #not in shows that ch is not htere in vowels
            c_count+=1
    return c_count

print(consonent_count("Education123"))


