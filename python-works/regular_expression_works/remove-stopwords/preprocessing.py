import re

sentence="Machine% learning# is a Subset@ of AI"
print("original sentence :",sentence)

sentence=sentence.lower()
print("lower cased :",sentence)

sentence=re.sub("[^a-z0-9 ]","",sentence)
print("noise removed :",sentence)

file_path="C:\\Users\\jojic\\OneDrive\\Desktop\\development-journey\\python-works\\regular_expression_works\\remove-stopwords\\stopwords.txt"
fr=open(file_path,'r',encoding="utf-8")
stop_words=[r.rstrip("\n") for r in fr]
filter_sentence=[w for w in sentence.split(" ") if w not in stop_words]
print("stop words removed :",filter_sentence)

refined_word=" ".join(filter_sentence)
print("refined sentence :",refined_word)

