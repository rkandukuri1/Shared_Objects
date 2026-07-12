# List is a Collection which can be Ordered and Changeable. Duplicates are allowed.

fruits_list = ["oranges", "bananas", "apples"]
#print(fruits_list)

# for x in fruits_list:
#     print(x)

# l = len(fruits_list)
# print(l)

# i =0
# while i < l:
#     print(fruits_list[i])
#     i = i + 1

fruits_list.insert(2, "mangos")
# print(fruits_list)

fruits_list_2 = ["grapes", "strawberries", "grapes"]

fruits_list.extend(fruits_list_2)  # Adds the new list at the end of existing list
print(fruits_list)

# fruits_list.pop(6) # Deletes the object at given index position
# print(fruits_list)

# fruits_list.remove("grapes")
# print(fruits_list)

# fruits_list.sort()
# print(fruits_list[2])  # Prints object at 2nd position
# print(fruits_list[2:5]) # Prints objects between 2nd and 5th positions where 5th position is excluded
# print(fruits_list[:5]) # Prints object from start till 5th position
# print(fruits_list[2:]) # Prints object from 2nd position till the end

fruits_list.clear()  # Similart to DELETE of Database
print(fruits_list)

del fruits_list  # Similart to DROP TABLE of database
print(fruits_list)