# list = ["apple","orange","banana","mango","orange"] #list is stored a multiple element in a single varibale
# list method
# 1.append()
# 2.clear()
# 3.copy()
# 4.count()
# 5.extend()
# 6.index()
# 7.insert()
# 8.pop()
# 9.remove()
# 10.reverse()
# 11.sort()


# list.append("kuwa")-> add a new element in last of the list

# list.clear()-> clear the all element in the list

# cp=list.copy()->copy the entire list 
# print(cp)

# print(list.count("orange"))->count get a parameter and check the array how many time the paramter in the array

# list2=["chery","pineapple","watermeloan"]
# list.extend(list2)->adding a another array in last of the list or combine a two array

# print(list.index("banana"))->it's return a index of first accurance

# list.insert(0,"first") -> it should get a two parameters. First params is where to push your element and 2nd one is what you push 'first one is index' and another one is (yourText,array,anything...)

# list.pop(2)->remove the value based on index-->thats means list.pop(2) is removed the 2nth index of list array

# list.remove("orange") ->this is remove the first accurence element in array besed get a params from you

# list.reverse() ->it's used to reverse a hole element in a array like decenting order

# list.sort() sorting a array like a-z based on first letter and 0-1 for number


# ************chatgpt************
# nums = [4, 2, 7, 2]

# nums.append(5)        # [4, 2, 7, 2, 5]
# nums.extend([8, 9])   # [4, 2, 7, 2, 5, 8, 9]
# nums.insert(1, 10)    # [4, 10, 2, 7, 2, 5, 8, 9]
# nums.remove(2)        # Removes first 2 → [4, 10, 7, 2, 5, 8, 9]
# last = nums.pop()     # Pops 9 → [4, 10, 7, 2, 5, 8]
# count = nums.count(2) # 1
# idx = nums.index(10)  # 1
# nums.sort()           # [2, 4, 5, 7, 8, 10]
# nums.reverse()        # [10, 8, 7, 5, 4, 2]
# copy_nums = nums.copy()  # Creates a new copy
# nums.clear()          # []


# print("\n",list)
# print("\n-------------after-----------------")

# if "banana" in list:
#     print("yes is there!")


# list[1]="graps"

# list[-3:]=["name","age","city"]

# del list[0] -> del keyword used to delete a element or entire array

# print(len(list))
# print("\n",list)

# list3=[x for x in list if "orange" in x]
# print(list3)

# list2=[1,2,3,4,5]
# list3=list+list2
# print(list3)



# *****************tuple********************
# tuple-> tuble also contain a multiple element in a single variable 
# tubles->tuble enclosed a (brackets)

# tuples=("apple","banana","mango","watermeloan","cherry")

# print(tuples)

# tuples-> tuples are unchangable and ordered and allows duplicates
# if you want to change a any specific element in tuples you should convert a type like tuples into list then you can change that
    # x = ("apple", "banana", "cherry")
    # y = list(x) -> convert tuples into list
    # y[1] = "kiwi" ->add a kiwi text in 1st index of y list
    # x = tuple(y) then convert list into tuple
    # print(x) 


# unpacked ->it's like Destructuring concept from js
# (s1,s2,*s3)=tuples #-> *s3 include a all balanced element

# print(s1) #-> it's hold a first index element in tuples
# print(s2) #-> it's hold a 2nd index element in tuples
# print(s3) #-> it's hold a balance element in tuples

# tuples=("kiwi","apple","watermelon","banana","apple")

# print(tuples.count("apple"))->it's return how many time apple accurance in a tuples
# print(tuples.index("kiwi")) -> return a first accurance index of kiwi

# ********************SETS*************

# sets={"apple","orange","banana","kiwi","apple","orange"} #creating a sets

# sets.add("mango")->add a new element in last of sets

# sets.clear()->clear the all elements

# newSets=sets.copy()->copy the entire sets and stored a new variable
# print(newSets)

# sets2={"apple","orange","banana","kiwi","mango"}
# print(sets2.difference(sets))->return a different element in sets2 compared in a sets
# newsets=sets2-sets->do same things in difference
# print(newsets)

# sets.discard("watermeloan") #->remove a all kiwi element in a sets
# sets.remove("watermelon")#->same as discard but raise a key error if you given element is not exist

# print(sets.pop()) ->remove the elements randomly and return a remived item and also removed the duplicates

# print(sets)



# *******************Dictionaries****************

# Dictionaries-->dictionaries likes objects in js 
# Dictionaries stored a values in  key and pairs like-> "name":"sujay"-> dictonary key also enclosed whit "" double or single quates
# Dictionaries are ordered, changable, do not allow a duplicates

# Dictionary Creation--->
# person={
#     "name":"sujay",
#     "age":23,
#     "city":"mayiladuthurai"
# }

# Dictionary method

# person.clear()-> clear the all element in a dictionary

# newPer=person.copy()->copy and store a dictionary

# ans=person.get("sujay")-> return a value based on you gives a key

# ans=person.items() #return a tuples in key and values

# ans=person.keys()->return a keys in a dictionary

# person.pop("name")->remove the value and key based on key what you give

# ans=person.popitem()->remove the last element and return that element
# print(person)



