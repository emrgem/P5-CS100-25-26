def safe_multiply(x, y):
    if isinstance(x,(int,float)) and isinstance(y,(int,float)):
        return x * y
    return 0
    
print(safe_multiply(5,3))
print(safe_multiply(4,"a"))


