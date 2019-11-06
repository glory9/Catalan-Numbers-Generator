def factorial(n):
    x = 1
    for num in range(1,n + 1):
        x = x * num
    return x

def catalan(c):
    up, down = factorial(2 * c), factorial(c)
    ans = up / ((c + 1) * down * down)
    return ans
    
def printCatalan(n):
    for i in range(n):
        print(catalan(i), end = "")
    return
        
s = int(input("How many catalan numbers do you want? "))
printCatalan(s)
