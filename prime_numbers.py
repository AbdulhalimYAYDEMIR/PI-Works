# Python 3.11.4 Language                                                                                                          #
#                                                                                                                                 #
# ALGORITHM                                                                                                                       #
# 1. Create Array that its first value 2, to collect prime numbers                                                                #
# 2. Create first counter that starts from 3.                                                                                     #
# 3. While Loop up to 600                                                                                                         #
#     3.1.  Create second counter to control                                                                                      #
#     3.2.  Control whether the number can be divide by previous prime numbers, if it is can not, increase second counter         #
#     3.3.  if second counter is equal to the length of prime numbers array, The number is prime number                           #
#     3.4.  when the number is divided by 100, if the division is 5, this number is prime number ,has 3 digit and starts with 5   #
#     3.5.  increase first counter                                                                                                #
###################################################################################################################################



#this counter is for checking all numbers
counter_1 = 3
# this array collect the prime numbers detected
primeNumbers = [2]

# While Loop for all numbers between 3 and 600
while counter_1 < 600:

    # this counter is for controlling whether the number can be divide by previous prime numbers
    counter_2 = 0

    # For Loop for all prime numbers detected
    for i in range(len(primeNumbers)):

        # if the number can not be divided prime numbers detected, counter is increased
        if counter_1 % primeNumbers[i] != 0:
            counter_2 += 1

    # if the number can not be divided all prime numbers detected, this number is added to array
    if counter_2 == len(primeNumbers):
        primeNumbers.append(counter_1)

        # when the number is divided by 100, if the division is 5, this number is prime number ,has 3 digit and starts with 5
        if int(counter_1/100) == 5:
            print(counter_1 )

    # for passing to next number
    counter_1 +=1
