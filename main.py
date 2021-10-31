# this is a prime generator
# it generates prime numbers that use principle of divide with previous ones
# it is not super optimize but needs only 1,5 seconds to generate all prime numbers between 0 and 100000
# enjoy and use code for your learning
from win10toast import ToastNotifier
import time
from pathlib import Path
import webbrowser

# the first 2 one prime numbers
startArray = [2, 3]

# the first number for test if prime
num = 3


# function for finding prime numbers
def getPrimeNumber():
    # declaring variables as global for future use
    global startArray
    global num

    # divide num with each prime number in startArray
    for prime in startArray:
        # % function return the rest of division
        if num % prime == 0:
            # exit loop because num is not prime
            break
    # if loop is never broken number is prime
    else:
        # append new  prime number to startArray
        startArray.append(num)


# the timer for testing optimization of program

# the while loop for finding numbers

howMany = int(input('Please enter the number to which you want to calculate prime numbers:\t'))
start = time.time()  # you can delete if you want
while True:
    getPrimeNumber()
    num += 1
    if num == howMany:
        break

end = time.time()
timeLapsed = end - start
toast = ToastNotifier()
print(startArray)
print(timeLapsed)
toast.show_toast('Prime completed', 'Hey your prime numbers has been calculated in ' + str(timeLapsed) + ' seconds')

# for saving into .txt file
saveOrNot = input('Type save to save prime numbers into .txt file:\t')
if saveOrNot == 'save':
    name = input('Type file name:\t')
    f = open(name + ".txt", "w")
    f.write(str(startArray))
    f.close()
    toast.show_toast('Saved successfully', 'Your prime numbers has been saved to: ' + name + '.txt')
