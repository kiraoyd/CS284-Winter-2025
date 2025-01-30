

def factorial_recursive(n):
    #base case, when to stop recursing
    if n == 0: #factorial of 0 is known to be 1
        return 1
    #recursive call to create a child
    answer = factorial_recursive(n-1) #child takes care of factorial n-1
    #once you have your kids answer, just multiply it by yours
    return n * answer

def main():
    #factorial 7 = 1 * 2 * 3 * 4 * 5 * 6 * 7
    n = 7
    result = factorial_recursive(n)
    print(f"The factorial of {n} is {result}")

main()
