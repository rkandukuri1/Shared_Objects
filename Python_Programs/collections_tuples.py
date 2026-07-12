# A Tuple is a collection which is Ordered and Unchangeable. Duplicates allowed.

colors_tuple = ("blue", "green", "yellow", "white")
print(colors_tuple)
# print(type(colors_tuple))

# print(colors_tuple[2])

# colors_tuple_2 = ("orange", "red")

# colors_tuple_3 = colors_tuple + colors_tuple_2
# print(colors_tuple_3)

# Workaround to add objects in a Tuple:
    # Assign the Tuple to a List and perform all required operations on the list 
    # Re-assign the list back to the Tuple

colors_list = list(colors_tuple) # Assign the Tuple to a List 
colors_list.insert(2, "black") # Perform all required operations on the list
print(colors_list)

colors_tuple = tuple(colors_list) # Re-assign the list back to the Tuple
print (colors_tuple)