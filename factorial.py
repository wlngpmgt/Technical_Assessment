#Function to calculate the factorial of a number
def factorialvalue(numbers):
    counter = 1
    for number in range(1,numbers+1):
        counter*=number
    return counter
    
#Function to check the number is prime
def primevalue(number):
    if number <= 1:
        return False
    
    for num in range(2,number):
        if number % num == 0:
            return False
    return True
