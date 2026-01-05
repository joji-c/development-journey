def vow_con_count(word):
    v_count=0
    c_count=0
    VOWELS="aeiou"
    for ch in word:
        if ch in VOWELS:
            v_count+=1
        else:
            c_count+=1
    return v_count,c_count


print(vow_con_count("hello"))

