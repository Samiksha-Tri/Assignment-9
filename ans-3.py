#Write a python script to print first N natural numbers in reverse order
n=int(input("enter number of times you want to print in reverse : "))
i=1
while i<=n:
    print(n-i+1,end=' ')
    i+=1
