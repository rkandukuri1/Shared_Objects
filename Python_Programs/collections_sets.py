# Sets -> unordered, Unchangeable, No Duplicates

fruits_set_1 = {"kiwi", "pears", "peaches", "pomegranade"}
#print(fruits_set_1)

# print(fruits_set_1[2]) # Raises Error

fruits_set_2 = {"bananas", "oranges", "kiwi"}

fruits_set_3 = fruits_set_1.intersection(fruits_set_2) # A INTERSECT B
print(fruits_set_3)

fruits_set_3 = fruits_set_1.union(fruits_set_2) # A UNION B
print(fruits_set_3)

fruits_set_3 = fruits_set_1.difference(fruits_set_2) # A - B
print(fruits_set_3)

fruits_set_3 = fruits_set_2.difference(fruits_set_1) # B - A
print(fruits_set_3)

fruits_set_3 = fruits_set_1.symmetric_difference(fruits_set_2) # (A - B) UNION (B - A)
print(fruits_set_3)