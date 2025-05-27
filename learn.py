list = ["apple","orange","banana","mango","orange"] #list is stored a multiple element in a single varibale
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
# list.extend(name)->adding a another array in last of the list or combine a two array

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


print("\n",list)
print("\n-------------after-----------------")

# if "banana" in list:
#     print("yes is there!")


# list[1]="graps"

# list[-3:]=["name","age","city"]

# del list[0] -> del keyword used to delete a element or entire array

print(len(list))
print("\n",list)

# list3=[x for x in list if "orange" in x]
# print(list3)

# list2=[1,2,3,4,5]
# list3=list+list2
# print(list3)

