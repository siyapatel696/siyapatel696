import random
import time
a=random.randint(0,9)
i=int(input("guess a number between 0-9:"))
while a!=i:
    print("wrong number")
    time.sleep(1)
    i=int(input("enter again:"))
print("number is",a)
print("correct guess")
    
