# print("What is your age?")
# age = input()                   #How to make an input()
# print("Your age is " + age)

#####################################

# def hello(name):
#   print('Hello ' + name + '!')  #Whats being displayed through function

# hello("Nikita")                 #The argument for the function
# hello("Beau")

################Nested Functions########################

# def test():
#   age = 8
#   print(age)

# test()

########################################

# def counter():
#   count = 0             #where the count starts

#   def increment():      #what the count has to do(increment-addup)
#     nonlocal count      #not a local variable
#     count = count + 1
#     return count        #return instead of print(because you dont want a.thing show yet)

#   return increment

# increment = counter()

# print(increment())
# print(increment())
# print(increment())
# print(increment())
# print(increment())

################For INT objects############################

# age = 8

# print(age.real)             #the real number (8)
# print(age.imag)             #imaginary number (hasnt been established = 0)
# print(age.bit_length())

##############Immutable Objects############################

# items = [1, 2]
# items.append(3)
# items.pop()
# print(id(items))

###########Loops#####################

# condition = True
# if condition == True:
#       print("The condition is True")
#       condition = False

######################################

# count = 0
# while count < 10:       #Keep printing sentence until 10th sentence
#     print("The condition is True")
#     count = count + 1   #OR count += 1

# print("After the loop")  #Print this when loop reached 10th sentence

#########FOR Loops######################

# for item in range(11):  #Print nums until 11
#     print(item)

# items = [1, 2, 3, 4]
# for item in enumerate(items):   #enumerate = indexed numbers
#     print(item)

########---OR this way---################

# items = [1, 2, 3, 4]  #OR ["beau", "syd", "quincy"]
# for index, item in enumerate(items):
#     print(index, item)  #Does the same as above

############Classes#####################
# class Animal:
#     def walk(self):
#         print("Walking...")

# class Dog(Animal):
#   def __init__(self, name, age):
#       self.name = name
#       self.age = age

#   def bark(self):      #'SELF' must be called for a class
#         print("woof!")

# roger = Dog("Roger", 8)

# print(roger.name)
# print(roger.age)
# roger.bark()
# roger.walk()

#############Modules####################

#importing other file########

# import dog

# dog.bark()

############# OR ###########

# from lib import dog  #inside a folder

# dog.bark()

############# OR ###########

# from lib.dog import bark

# bark()

##############################
# import math 

# print(math.sqrt(4))

##########  OR  ##############
# import math from sqrt

# print(sqrt(4))

###########Accepting Arguments##########
# import sys

# name = sys.argv[1]

# print("hello " + name)

##############################

# import argparse

# parser = argparse.ArgumentParser(
#   description='This program prints the name of my dogs'
# )

# parser.add_argument('-c', '--color', metavar ='color', required=True, help='the color to search for')

# args = parser.parse_args()

# print(args.color)

############LAMBDA###############################

# lambda num : num * 2

# multiply = lambda a, b : a * b

# print(multiply(2, 4))

##############Map,Filter, Reduce#############

# numbers = [1, 2, 3]

# def double(a):
#   return a * 2

# result = map(double, numbers)  #Map for list of items

# print(list(result))

############  OR   ##############################

numbers = [1, 2, 3]

double = lambda a : a * 2

result = map(double, numbers)  #Map for list of items

#OR result = map(lambda a : a * 2, numbers)

print(list(result))

