def count_vowels(s):
    v_count=0
    VOWELS="aeiou"                #we use all caps to show that this variables value is a constant
    for ch in s.casefold():   
        if ch in VOWELS:          #in shows that ch is there in vowels
            v_count+=1
    return v_count
    
print(count_vowels("hello"))
print(count_vowels("Education"))
