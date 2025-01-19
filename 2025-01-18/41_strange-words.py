my_string = 'hello world'
def solution(s):
    words = s.split(" ")
    answer = []
    for word in words: 
        new_word = ""
        for index, ch in enumerate(word): 
            if index % 2 == 0: new_word += ch.upper()
            else: new_word += ch.lower()
        answer.append(new_word)

    return " ".join(answer)
        
print(solution(my_string))

    
      
