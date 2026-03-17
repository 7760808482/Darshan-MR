#Create a tuple with 5 elements.
my_tuple=(1,2,3,4,5)
#Perform slicing on the tuple to extract the second and third elements.
print(my_tuple[1:3])
#Concatenate the tuple with another tuple.
my_tuple2=(6,7,8,9,10)
print(my_tuple+my_tuple2)
#Try to modify one of the elements. What happens?
my_tuple[0]=1
print(my_tuple)
print(type(my_tuple))