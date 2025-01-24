def solution_wrong(n, lost, reserve):
    for i in lost:    # VERY DANGEROUS : if we use sets, this is okat but we gotta make a copy of a list if we use lists
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
    cnt = n-len(lost)
    for i in lost:
        if i - 1 in reserve:
            reserve.remove(i - 1)
            cnt+=1
        elif i + 1 in reserve:
            reserve.remove(i + 1)
            cnt+=1
        else:
            continue

    return cnt

def solution(n, lost, reserve):
    # Make copies to avoid modifying the original lists
    lost = sorted(lost)  # Sorting ensures we handle students in order
    reserve = sorted(reserve)  # Sorting ensures consistency

    # Step 1: Remove students who both lost and have an extra uniform
    lost_copy = lost[:]  # Create a copy of lost to safely iterate over
    for i in lost_copy:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)

    cnt = n - len(lost)  # Students who already have a uniform

    # Step 2: Try to lend gym uniforms
    for i in lost:
        if i - 1 in reserve:  # Check if the previous student can lend
            reserve.remove(i - 1)
            cnt += 1
        elif i + 1 in reserve:  # Check if the next student can lend
            reserve.remove(i + 1)
            cnt += 1

    return cnt



def solution(n, lost, reserve):
    # Convert lists to sets for easy comparison
    lost_set = set(lost)
    reserve_set = set(reserve)
    
    # Students who lost and have an extra uniform
    intersection = lost_set & reserve_set
    lost_set -= intersection
    reserve_set -= intersection
    
    # Iterate through sorted reserve students to lend uniforms
    for r in sorted(reserve_set):
        if r - 1 in lost_set:
            lost_set.remove(r - 1)  # Give to the left neighbor
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)  # Give to the right neighbor
    
    # Return the number of students who can participate
    return n - len(lost_set)

# Example test cases
print(solution(5, [2, 4], [1, 3, 5]))  # Output: 5
print(solution(5, [2, 4], [3]))  # Output: 4
print(solution(3, [3], [1]))  # Output: 2


# Test case
n = 5
lost = [2, 4]
reserve = [1, 3, 5]
print(solution(n, lost, reserve)) 
            

