n=5
def fibonacci(n):
    if n <=1:
        return n
    return fibonacci(n-1)+ fibonacci(n-2)

print("numero en fibonacci",fibonacci(n))    