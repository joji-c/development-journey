class Anagram:
    def solution(self,word1,word2):
        self.is_anagram=True
        if len(word1)!=len(word2):
            return False
        for ch in word1:
            self.count_word1=word1.count(ch)
            self.count_word2=word2.count(ch)
            if self.count_word1!=self.count_word2:
                self.is_anagram=False
                break
        return self.is_anagram

instance=Anagram()
print(instance.solution("listen","silent"))
