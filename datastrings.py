from ast import Is
import string
# 

#     #string formating
# name = "Angela"
# age =55
# print("Her name is " + name)

# print("Her name is %s and she is %d" % (name,age))

# sampleList = ["Angela","love","dove"]
# print("some text %s" % sampleList)
# print("text %s" % sampleList)

# name = "Angela"
# time = "10.00am"
# currency = "KES"
# balance = 5000.00

# feel = "excited"
# course = "coding"

# print(f"I am super {feel} about {course}")

# print(f"Hello {name}, confirmed your balance at {time} was {currency} {balance}")



# #Lists
# list = ["Ann","Apple",2,46,30.9,1.3,"student"]
# print(list)

# print(list[0])
# print(list[3])

# list.append("Mike")
# print(list[7])

# print(list)

# list2 = ["a","b",2,4,"o","stop"]
# print(list2)

# list2.append("start")
# print(list2[6])

# print(list2)






#Conditionals
age=18
movie ="Trinkets"

if (age == 18):
    print("Customer can book a ticket for "  +  movie)

if(age>=18):
    print("Customer can get a sit to watch "  + movie) 

age=16
height =5
#and -the two conditions must be true for the test to pass.
if(age>=16 and height >= 5):
    print("Customer can have a drink") 

#or -for the test to pass,only one condition is required to be true.
elif(age < 16 or height < 5):
    print("Cannot have any drink")

else:
     print("Something went wrong") 



string1 = "Angela"
string2 = "4.5"
string3 = "0"
string4 = "true"
string5 = "6"
print(string1 +"is also saying "+ string4) 

#concatination ("")
#concatination is adding two strings

number1 = 4.5
number2 = 0
number3 = 5
number4 = -4
number5 = 123453567890987
print(number1+number3)

#boolean - its a state identifier
IsStudentActive = True
print(IsStudentActive)

isGraduate = False
print(isGraduate)

age = 45

if (age>45):
    print("yes")

    cup = "water"
    cup = "sand"

crate = ["sand","water",4,6,7,2]#a list is a variable that can hold multiple data types
print(crate[1])

crate.append("Ann")
print(crate[5])


#length of a string
string ="I am a string"
print(len(string))
print(string.index("a"))

#count of a string 
print(string.count("x"))

print(string[1:6] )

print(string.upper())
string2 = "UPPERCASE"
print(string2.lower())

#to reverse a string
print(string[::-1])

print(string2.startswith("a"))
print(string2.endswith("E"))

#OPERATORS-something that allows you to perform an action
value1 = 4
value2 = 7
print(value1+value2)

print(value1-value2)

print(value1%value2)

print(value1 * value2)

print(value1/value2)

#assignment operators
Variable = 5

#comparison operator
print(value1==value2)

#isGreater
print(value1>value2)

#isGreaterorEqual
print(value1>=value2)

#remainder
a=12
b=3
print(a%b)

voice = "shout"
print(voice)
print(voice *5 )

list = [1,2,3,4,5,6]
print(list * 5)

x = [1,2,3,4]
y = [5,6,7,8]
print(x+y)

age = 35
age = age + 1
print(age)
age+=1
print(age)

#conditionals - an expression that will only be expressed when a certain condition is met
age =17.5
movie ="scary-terry"
if (age >= 18):
    print("Customer can purchase ticket for a movie" + movie)
    if(age < 18):
     print("Customer is not allowed to watch this movie" + movie)

age = 16
height = 5
if (age>=18 and height>=5):
    print("person an get on the")
# if (age<18 or height<5):
elif(age<18 or height<5): 
     print("person cannot get on the")
            
         





 