# learn condtional statement*****************************

#************************ if else statement 

# a=int(input("enter a number: "))
# b=int(input("enter a number: "))

# if a>b:
#     print( a," is bigger than ",b)
# elif a==b:
#     print(a,b,"both are equal")
# else: 
#     print( b," is bigger than ",a)

# print( a," is bigger than i f",b) if a>b else print( b," is bigger than else",a)
# syntax print("if statement") if condition(a>b) else print("else statement")
# like--> 10<5 ? console.log("if") : console.log("else")

# and -> &(js)
# or -> |(js)
# not -> !(js)

# if a==b and a>b:
#     print("a==b and a>b both condtion need to be true either one condtion is false do not do the if statement")
# if a==b or a>b:
#     print("condtion a==b or a>b either one condtion is need to be true ")
# if not(a==b):
#     print("a==b must be a not equal")


#****************************** match statement

# other language it name is switch statement in python it name is match nothing different act like a same thing
# a=1
# match a:
#     case 1 if a<5: # case value and match value be a same and then if condition also to be true
#         print("run a 1st case")
#     case 2:
#         print("run a 2nd case")
#     case 3:
#         print("run a 3rd case")
#     case 4:
#         print("run a 4th case")
#     case 5:
#         print("run a 5th case")
#     case _: # act like a default case  
#         print("no match")

# loop********************

# i=12
# while i<10:
#     print(i)
#     i+=1
# else: # in python you can use else for a false statement 
#     print(i,"is bigger than or equal 10")

# i=0
# while i<10:
#     print(i)
#     if i==5:
#         break #you want to end the loop i is to be a 5. That case you use if and break the condtion using break keyword
#     i+=1 #end of the loop increment operation

# i=0
# while i<10:
#     i+=1
#     if i==5:
#         continue #if you want skip any element using countine keyword
#     print(i)
#     # i+=1 #if i write a increment operation here it's not working


# for loop******************

arr=["apple","banana","graps","orange","mango"]

# for res in arr: # get a each element in a list and store a res varibale 
#     print(res) #every time run a loop res have a different element from list

# for res in "apple":
#     if res=="l":
#         break #if you want break when l is come you can use break like while loop
#     print(res)

# for res in arr:
#     if res=="orange":
#         break
#     print(res)

for res in range(5,50,5): # 1st params is starting value, 2nd is ending value, 3rd is increment value like res+=5.
    print(res)
else:
    print("finished") #for loop also have a else statement

