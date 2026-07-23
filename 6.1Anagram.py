#using sorting method
# word1 = "heart"
# word2 = "earth"
# sorted_1 = sorted(word1)
# sorted_2 = sorted(word2)
# if sorted_1 == sorted_2:
#     print("Words are anagrams.")
# else:
#     print("Words are not anagrams.")

#using counter -> counter counts how many times each letter appears
# from collections import Counter
# word1 = "listen"
# word2 = "silent"
# if Counter(word1) == Counter(word2): #time complexity O(n)
#     print("Anagram")
# else:
#     print("Not Anagram")

# def is_anagram(word1, word2):
#     return sorted(word1.lower()) == sorted(word2.lower())

from collections import Counter

def is_anagram(word1, word2):
    return Counter(word1.lower()) == Counter(word2.lower())
word1 = "heart"
word2 = "earth"
print(is_anagram(word1, word2)) 