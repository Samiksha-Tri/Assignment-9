# Write a python script to print first N odd natural numbers in reverse order
n=int(input("enter number of times you want to print odd natural number in reverse : "))
i=n*2-1
while i>0:
    print(i,end=' ')
    i-=2
