#A four-digit integer is given. Find the number of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable "var_int".
x=int(input("x=",))
a=x%10
b=x//10%10
c=x//100%10
d=x//1000
sum=0
if a%2==0:
    sum+=1
if b%2==0:
    sum+=1
if c%2==0:
    sum+=1
if d%2==0:
    sum+=1
print(sum)