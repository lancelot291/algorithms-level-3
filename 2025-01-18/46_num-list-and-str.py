def solution(s):

    num_dict = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    for key, value in num_dict.items():
        s = s.replace(key, value)

    return int(s)
    
    
'''    s = s.replace("zero", "0")
    s = s.replace("one", "1")
    s = s.replace("two", "2")   
    s = s.replace("three", "3")
    s = s.replace("four", "4")
    s = s.replace("five", "5")
    s = s.replace("six", "6")
    s = s.replace("seven", "7")
    s = s.replace("eight", "8")
    s = s.replace("nine", "9")
    return int(s)   '''

s = "one4seveneight"
print(solution(s))   
