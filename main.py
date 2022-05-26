# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram():
    word_1 = input("Type in word")
    word_2 = input("Type in another word")

    if(sorted(word_1) == sorted(word_2)):
        return True
    else:
        return False
find_anagram()

