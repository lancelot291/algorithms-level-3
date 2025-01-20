def solution(s):
    answer_list = []
    for i in range(len(s)):
        flag = 0
        for j in range(i-1, -1, -1):
            if s[i] == s[j]:
                answer_list.append(i-j)
                flag+=1
                break
        if flag == 0:
            answer_list.append(-1)

    return answer_list

def solution_2(s):    
    answer_list = []
    for i, ch in enumerate(s):
        if ch in s[:i]:
            answer_list.append(i - s[:i].rindex(ch))
        else:
            answer_list.append(-1)

    return answer_list

def helper(i, s):
    for j in range(i-1, -1, -1):
        if s[i] == s[j]:
            return i-j
    return -1


def solution_3(s):
    answer_list = []    
    for i, ch in enumerate(s):
        if ch in s[:i]:
            answer_list.append(helper(i, s))
        else:
            answer_list.append(-1)

    return answer_list

def solution(s):
    # Dictionary to store the last seen index of each character
    last_seen = {}
    # List to store the result
    result = []
    
    # Iterate through the string
    for i, char in enumerate(s):
        if char in last_seen:
            # If the character was seen before, calculate the distance
            result.append(i - last_seen[char])
        else:
            # If the character is appearing for the first time, append -1
            result.append(-1)
        
        # Update the last seen index of the current character
        last_seen[char] = i
    
    return result

def solution(s):
    def find_previous_occurrence(index, s):
        for j in range(index - 1, -1, -1):
            if s[index] == s[j]:
                return index - j
        return -1
    
    return [find_previous_occurrence(i, s) for i in range(len(s))]



s = 'banana'
print(solution(s)) # [-1, -1, 1, 3, 1, 5]
print(solution_2(s)) # [-1, -1, 1, 3, 1, 5]
print(solution_3(s)) # [-1, -1, 1, 3, 1, 5] 

# asfd



        