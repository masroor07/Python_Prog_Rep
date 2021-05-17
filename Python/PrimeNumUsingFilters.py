#we define a function
def prime(x):
    #for loop with range from 2 to x
    for n in range(2,x):
        #if thx is divisible by any number from 2 to x, print false
        if x%n==0:
            return False
        #return true
        else:
            return True
        #we filter the function and pass arg
filtered= filter(prime, range(300))
print("prime numbers are:", list(filtered))
