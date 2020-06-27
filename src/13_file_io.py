"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# text_file = open("foo.txt", "r")
# read_file = text_file.read()
# print(read_file)
# text_file.close()

with open("foo.txt", "r") as foo:
    read_file = foo.read()
    print(read_file)


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

with open("bar.txt", "w") as bar:
    bar.write("First line of text\n")
    bar.write("Second line of text\n")
    bar.write("Third line of text\n")
    bar.close()

with open("bar.txt", "r") as bar:
    read_file = bar.read()
    print(read_file)