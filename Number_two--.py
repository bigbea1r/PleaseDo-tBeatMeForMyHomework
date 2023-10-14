def maxnumber(a):

    a.sort(key=lambda x: x * 3, reverse=True)

    m = len(max(a, key=len))

    a.sort(key=lambda x: x * m, reverse=True)
    
    result = ''.join(a)

    result = int(result)
    
    return result