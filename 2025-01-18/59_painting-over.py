def solution(n, m, section):
    count = 0  
    current_position = 0

    for space in section:
        if space > current_position:
            count+=1
            current_position = space+m-1

    return count





        