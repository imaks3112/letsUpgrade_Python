//primeOrNot.py file.

%%writefile primeOrNot.py

def prime(number):
    return number
	
	
	
//

import primeOrNot

primeOrNot.prime("9")







//testPrimeOrNot.py file

%%writefile testPrimeOrNot.py

import unittest
import primeOrNot

class testPrime(unittest.TestCase):
    def isPrime(self):
        self.ino = "9"
        for i in range(2, self.ino):
            if (self.ino % i) == 0:
                print(self.ino, "is not a prime number")
                break
            else:
                print(self.ino, "is a prime number") 
  
    
if __name__ == "__main__":
    unittest.main()