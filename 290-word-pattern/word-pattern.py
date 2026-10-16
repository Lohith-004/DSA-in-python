class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(words) != len(pattern):
            return False

        word_to_char = {}
        char_to_word = {}

        for ch,word in zip(pattern, words):
            if ch in char_to_word and char_to_word[ch] != word:
                return False
            
            if word in word_to_char and word_to_char[word] != ch:
                return False

            word_to_char[word] = ch
            char_to_word[ch] = word

        return True