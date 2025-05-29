# functions 

# python function nothing else same as a js function or other progamming function

# def functionName(): -> def keyword used to create a function 
    # function code  ->function code type here and follow the indentation

# functionName() -> function call

# def getName(name):
#     print("my name is: ",name)

# getName("sujay")

# Arbitrary Arguments, *args
# Arbitrary Argiments is you can take n number of arguments in a single parameter. that parms contain a values as a tuples
# you don't know how many arguments you take that's cases used a Arbitary Arguments

# def getNames(*names):
#     for x in names:
#         print("my name is:",x)

# getNames("vijay","ajith","surya","kamal")


# keyword Arguments
# you can send a argument with a key 

# def NamesKey(name3,name1,name2): #if you used a key for a arguments then params order does't matter. you can suffle user params 
#     print(name3)

# NamesKey(name1="vijay",name2="ajith",name3="surya")

# def fullName(**name): #double star for keyword arguments
#     print("My First name is:",name["fname"]) #you access the values like dictonary access concept
#     print("My Last name is:",name["lname"])

# fullName(fname="Ajith",lname="kumar")

# default parameter********************
 #you can give a default params like you call the function but you not give the arguments that case function get a default params value
# def check(name="sujay"):
#     print("i'm ",name)

# check("ajith") #output is "I'm ajith"  if you give a arguments it's fine. it'll print what you gave
# check() #output is "I'm sujay" because you just call the function but you not gave any arguments so name take a default value

# pass statement
    #function can't be empty.if your function is empty it's throw a error 
    # that case you avoid error used pass keyword
    #  but some case you want a function be empty

# def empty():
#     pass #in this function can't have a any code 

# def getOne(num,/): #you set how many argument you want. / ->used for restricted the another argument
#     print(num)

# getOne(num=5) #it's do not allow a keyword argument


# lambda function ************
# lambda function called anonymous function and it's a single line function automatically return a value

# add=lambda a,b:a+b
# sub=lambda a,b:a-b
# mul=lambda a,b:a*b
# div=lambda a,b:a/b

# print(add(5,5))
# print(sub(5,5))
# print(mul(5,5))
# print(div(5,5))