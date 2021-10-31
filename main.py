# this is a prime generator
# it generates prime numbers that use the principle of dividing with previous ones
# it is not super optimized, but needs only 1.5 seconds to generate all prime numbers between 0 and 100000
# enjoy and use the code for your learning

import time

# the first two prime numbers
startArray = [2, 3]

# the first number for testing if prime
num = 3


# function for finding prime numbers
def getPrimeNumber():

    # divide num with each prime number in startArray
    for prime in startArray:
        # '%' operator returns the remainder of a division
        if num % prime == 0:
            # exit loop because num is not prime
            break
    # if loop is never broken, the number is prime
    else:
        # append new  prime number to startArray
        startArray.append(num)




# the while loop for finding numbers

howMany = int(input('Please enter the number to which you want to calculate prime numbers:\t'))
start = time.time()
while True:
    getPrimeNumber()
    num += 1
    if num == howMany:
        break

# the timer for testing the optimization of the program
end = time.time()
timeLapsed = end - start
print()
print(startArray)
print('\nHey, your prime numbers have been calculated in ' + str(timeLapsed) + ' seconds')

# for saving into .txt file
saveOrNot = input("Type 'save' to save prime numbers into .txt file:\t")
if saveOrNot == 'save':
    name = input('Type file name:\t')
    f = open(name + ".txt", "w")
    f.write(str(startArray))
    f.close()
    print('\nSaved successfully to: ' + name + '.txt')
