import os

os.chdir("/Users/preethisivakumar/Desktop/sample")




print(os.getcwd())
print(os.listdir())


# Source file path
source = "hello.txt"

# Destination file path, including the filename
destination = "/Users/preethisivakumar/Desktop/hello.txt"

# Rename or move the file
os.rename(source, destination)

os.chdir("/Users/preethisivakumar/Desktop")
print(os.getcwd())
print(os.listdir())
os.chdir("/Users/preethisivakumar/Desktop/sample")




print(os.getcwd())
print(os.listdir())
print(os.path.join('folder', 'subfolder'))
