"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
def read_file():
	with open('foo.txt', 'r') as f:
		read_data = f.read() 
		print(read_data)

read_file()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
def write_file():
	value = ('Testing testing testing\nHello there mister!!!\nFrom python terminal')
	with open('bar.txt', 'w') as f:
		s = str(value)
		f.write(s)

def read_createdfile():
	with open('bar.txt', 'r') as f:
		read_data = f.read()
		print(read_data)

write_file()
read_createdfile()
