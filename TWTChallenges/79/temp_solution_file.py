def solution():
    T = int(input())          
    for _ in range(T):        
        string = str(input())
        key = str(input())
        result = ""
    
        for _ in string:
            result += chr(ord(_)^ord(key))
    
        
        print(result)