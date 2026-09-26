'''
#simple if
a = int(input("Enter a Number : "))
if a==10:
    print("Ok")

#if - else
#simple if
a = int(input("Enter a Number : "))
if a==10:
    print("Ok")
else:
    print("No")

#odd or even
a = int(input("Enter a number"))
if a%2==0:
    print("Even")
else:
    print("Odd")

#check the given number is multiple of 3 or not :
    #if multiple of 3 means print("Yes")
    #or print("No")
a=int(input("enter a number"))
if a%3==0:
    print("yes")
else:
    print("no")

#check the given character is vowel or consonant
ch = input("Enter a character : ")
if ch>='a' and ch<='z':
    if ch=='a' or ch=='i' or ch=='e' or ch=='o' or ch=='u':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid Character")

ch = input("Enter a character : ")
if ch>='a' and ch<='z':
    vowel = ['a','i','e','o','u']
    if ch in vowel:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid Character")

n = int(input("Enter a number :"))
if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:
    print("Zero")
    
#for loop
for i in range(1,10,2):
    print(i)

#print the even number from 1 to 100

for i in range(1,101,1):
    if i%2==0:
        print(i)

for i in range(2,101,2):
    print(i)
'''
#from 1 to 100 (2,6,10)
for i in range(2,101,2):
    if i%6==0 and i%10==0:
        print(i)


for i in range(100,1,-2):
    if i%6==0 and i%10==0:
        print(i)
















