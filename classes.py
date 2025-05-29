# # classes -> classe like a blue print in your application

# # class Myclass: #class keyword used to create a class
# #     x=10 # properties -> you create a variable inner the class is called properties 

# #     def myfun(): # you create a function inner the classes is called a method
# #         print("method from class")

# # obj=Myclass()

# # print(obj.x)



# # class calculator:
    
# #     def add(self,num1,num2):
# #         print(num1+num2)

# #     def sub(self,num1,num2):
# #         print(num1-num2)

# #     def mul(self,num1,num2):
# #         print(num1*num2)

# #     def div(self,num1,num2):
# #         print(num1/num2)

# # math=calculator()

# # math.add(5,5)
# # math.sub(20,15)
# # math.mul(5,5)
# # math.div(10,2)

# # class myClass:
# #     def __init__(self,name1,name2): #this is a constructor 
# #         self.fname=name1 #self represent a class name(this class)
# #         self.lname=name2
    
# #     def fullname(self):
# #         return 'my name is '+self.fname+self.lname
        
# # obj=myClass("sujay","selvan")

# # print(obj.fname)
# # print(obj.lname)
# # print(obj.fullname())

# # # you can change a value after the constructor create or after object create
# # obj.fname="ajith"
# # obj.lname="kumar"

# # print(obj.fullname()) #my name is ajithkumar

# # # you also delete a properties
# # del obj.fname

# # print(obj.fullname()) #getting a error because fname was deleted

# # # you want to declare a empty class used a self keyword

# # class empty:
# #     pass


# # inheritance*********************************

# # syntax only change other than all are same like as js

# class Parent:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
    
#     def fullname(self):
#         return self.fname+self.lname

# class child(Parent): #the way of extents or merge or combine a two classes
#     def father(self):
#         return 'my father name is '+self.fullname()
    
# obj=child("senthamil","selvan") # create a object for child class and this object can access a parent and child classes properties and method
# obj1=Parent("ajith","kumar") # create a object for parent class only this object only access a our properies and method can't access a child class method and properties

# print(obj.father())
# print("my full name is"+obj.fullname())
# print(obj1.fullname())

# #child class also create a constructor and should allownce a parent class

# class child(Parent):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname) #you can use super or Parent class name both are do same
