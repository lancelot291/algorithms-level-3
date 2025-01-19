def solution(s, n):
    new_s = []
    for ch in s:
        if ch.isupper():
            new_s.append(chr((ord(ch)-65 + n) % 26 + 65))
        elif ord(ch) == 32: 
            new_s.append(" ")
        else:
            new_s.append(chr((ord(ch)-97 + n) % 26 + 97))

    return "".join(new_s)

print(solution("a B z", 1))