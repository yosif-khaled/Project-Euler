#calculating prime factors for a number

i = 2
print ("Enter Number :")
n = int(input())
while True:
    if n%i == 0:
        n = n/i
        print(i)
    elif n == 1:
        break
    i += 1


# you need to find a way to decrease the value of n (sorted)
# because when I add n = n/i the value of n doesn't change (sorted)
# new problem don't do well with numbers up to the power 2 (arised)
# don't do well with numbers up to the power 3 either (arised)
# doesn't display the right values up to power x where x > 3 (arised)
# will come back later from another angle
# cause of problem is single iteration increment
# note: more than one iteration will slow the program down
# note: test iterating thrgh values (1 to 100)