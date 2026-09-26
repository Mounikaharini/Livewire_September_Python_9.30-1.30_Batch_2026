#operators

#arithmetic (+ - * / % // **)
print(10+90)
print(90-12)
print(2*9)
print(2/4)
print(2//4)
print(5%2)
print(2**3)

#assignment (= += -= *= /= //= %=)
c = 10
print(c)#10
c+=15
print(c)#25
c-=5
print(c)#20
c*=4
print(c)#80
c/=5
print(c)#16
c = int(c) #type casting
c//=5
print(c)#3
c%=8
print(c)#3

#comparision (== != < > <= >=)
print(10==10)
print(10!=100)
print(10<19)
print(19>90)
print(19>=19)
print(19<=19)

#logical(and or not)
print(10>10 and 10>20)
print(10>=10 or 10>20)
print(not(10>10 and 10>20))

#bitwise (& | ~ ^ << >>)
print(5&2)
print(5|2)
print(~2)
print(~(-2))
print(5^2)
print(5<<2)
print(5>>2)

#membership (in not-in)
a = [1,2,34,3,2,3,2,3,9,4,4,5,31]
print(5 in a)
print(5 not in a)

#identity (is is-not)
a = 1
b = 2
c = 1
print(a is c)
print(a is not b)




















