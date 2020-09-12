def isPrime(x):
    for n in range(2,x):
        if x % n == 0:
            return False
        else:
            return True

fltrObj=filter(isPrime, range(2500))
print ('Prime numbers between 1-2500:', list(fltrObj))