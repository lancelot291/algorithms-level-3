
import re

def solution(babbling):
    # Define the only valid sounds that can be used
    valid_sounds = ["aya", "ye", "woo", "ma"]
    
    # Create a regex pattern that allows only valid 
    # sound combinations without consecutive repeats
    pattern = re.compile(r'^(aya|ye|woo|ma)+(?!\1)$')

    count = 0  # Counter for valid words
    for word in babbling:
        # Check if the word consists only of the allowed 
        # sounds and doesn't repeat the same sound consecutively
        if pattern.fullmatch(word):
            count += 1

    return count

# Test cases
print(solution(["aya", "yee", "u", "maa"]))  # Output: 1
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))  # Output: 2


def solution(babbling):
    
    double = ["11", "22", "33", "44"]
    new_words = [0] * len(babbling)
    for i in range(len(babbling)):
        new_words[i] = babbling[i].replace("aya", "1")
        new_words[i] = new_words[i].replace("ye", "2")   
        new_words[i] = new_words[i].replace("woo", "3")
        new_words[i] = new_words[i].replace("ma", "4")
        # print(f'new words are {new_words[i]}')
        
    new_words_2 = new_words.copy()
    for word in new_words_2:
        for i in range(4):
            if double[i] in word:
                new_words.remove(word)
                break


    cnt = 0
    for word in new_words:
        if word.isdigit():
            cnt += 1

    return cnt

babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]

print(solution(babbling)) 

