def factorial(n):
    if n < 0:
        return -1 #error flag
    if n == 0:
        return 1

    #If the n value is valid and > 0
    digit = 1
    product = 1

    while digit <= n:
        product = product * digit
        #print(f"Digit: {digit}") #work
        digit = digit + 1

    return product

def main():
    n = -7
    factorial_result = factorial(n)
    if factorial_result < 0:
        print("Error")
    else:
        print(f"Factorial of {n} is: {factorial_result}")

main()