# problem:6
# Input some comma seprated numbers : 3,5,7,23                       
# List :  ['3', '5', '7', '23']                                      
# Tuple :  ('3', '5', '7', '23')  


values = input("Input some comma seprated numbers : ")#input value taking
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)