# here a,b,c are variables and 1,10 and output of a+b are constants
a = 1
b = 10

c = a+b
print(c)

# data types:
# int - numbers 1,2,3,4....
# float - 1.2,3.5,0.3
# bool - True or False
# str - "vaishnavi", "hello"

print(type(a))

num = 1.5
name = "vaishnavi"
value = True
print(type(num))

print("type of num before typecasting: ", type(num))
num = int(num)
print("type of num after typecasting: ", type(num))