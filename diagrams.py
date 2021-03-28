import os

directory_to_check = "." # Which directory do you want to start with?

def my_function(directory, file):
    
      print("Listing: " + directory)
      print("\t-" + "\n\t-".join(os.listdir("."))) # List current working directory
      print("python3 " + file)

# Get all the subdirectories of directory_to_check recursively and store them in a list:
directories = [os.path.abspath(x[0]) for x in os.walk(directory_to_check)]
directories.remove(os.path.abspath(directory_to_check)) # If you don't want your main directory included
files = [os.path.basename(y[0]) for y in os.walk(directory_to_check)]
files.remove(os.path.basename(directory_to_check)) # If you don't want your main directory included

for i in directories:
    for j in files:
        os.chdir(i)         # Change working Directory
        my_function(i, j)      # Run your function