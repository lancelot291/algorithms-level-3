def solution(a, b, n):
    total_colas = 0  
    # result
    while n>=a:
        # the condition to exchange colas
        total_colas+=(n//a)*b
        # adding the numers of colas that we got from exchanging
        new_colas = (n//a)*b
        #colas that we got from exchanging
        n = new_colas + (n%a)
        #replace n to the number of colas we got after the exchange

    return total_colas
# returning the total number of colas that we got from exchanging
    
 