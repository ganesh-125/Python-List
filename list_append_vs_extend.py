# Define a Empty list
List1=[]
# List with values
List2=[1,2,3]
# Appending the b into a
List1.append(List2)
print("Append :",List1)



# Define a Empty list
List1=[]
# List with values
List2=[1,2,3]


# extend v/s append 
List1.extend(List2)
print("Extend :",List1)



# Output
# Append : [[1, 2, 3]]
# Extend : [1, 2, 3]