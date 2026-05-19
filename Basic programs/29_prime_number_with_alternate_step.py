# Practice Problem: Write a program to find all prime numbers up to 20, but only print every second (alternate) prime number found.

# Exercise Purpose: This exercise combines “Nested Loops” (to check for primality) with “Step Logic.” It requires the programmer to first identify a subset of data and then apply a secondary filter, a common task in data reporting.



primes=[]

for num in range(2,21):
    
    for j in range(2,int(num ** 0.5)+1):
        
        if num % j == 0 :
            break
        
    else:
        primes.append(num)
            
            
alternate_prime=primes[::2]

print(alternate_prime)            