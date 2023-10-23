#A four-digit integer is given. Find the sum of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_odd" and assign it 0.

#Find the sum of the odd digits in the variable "var_int".
x=int(input("x= ",))
a=x%10
b=x//10%10
c=x//100%10
d=x//1000
sum=0
if a%2==1:
    sum+=a
if b%2==1:
    sum+=b
if c%2==1:
    sum+=c
if d%2==1:
    sum+=d
print(sum)
