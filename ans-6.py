#Write a python script to print first N even natural numbers
n=int(input("enter number of times you want to print even natural number: "))
i=2
while i<=n*2:
    print(i,end=' ')
    i+=2
