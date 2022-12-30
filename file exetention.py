

# Input the Filename: abc.java                                                                                  
# The  extension of the file is : 'java'


filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))