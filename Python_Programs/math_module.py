def biggest2(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2
    
def biggest3(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3
    
def factorial(n1):
    result = 1
    for i in range(n1):
        j = i + 1
        result = result * j
    return result
