import os

filename = "./data/data.txt"
my_file = open(filename, "r")  # r for "read"
# Can you put the contents of this file in the form of a list in which each element is a sentence ? (Use .split() for example...)
content = my_file.read().split(' ')
#print(content)
my_file.close()


# Get Path Name
path = os.path.abspath("./data")

#print(filename)
#print(path)
#print(type(path))

# Manage Specific file under specified path
filename = path+"/data.txt"
my_file = open(filename, "w")  # w for "write"
my_file.close()

# Get all files from specified path
os.path.basename(path)

# Put all the .txt files from the data/ directory into a variable.
# Then, copy the content of all the files from this variable into a file in data/ that you will name final.txt.
for path, dirs, files in os.walk(path):
    for filename in files:
        if filename.endswith(".txt") and filename != "final.txt":
            file_path = os.path.join(path, filename)

            with open(file_path, 'rb') as f:
                content = f.read().split()

            # Decode the content from bytes to strings, ignoring errors
            # [expression for item in iterable]
            content = [word.decode('utf-8', errors='ignore') for word in content]


            with open(os.path.join(path, "final.txt"), "a") as my_file:
                my_file.write(' '.join(content) + '\n')