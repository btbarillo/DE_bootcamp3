#close()	Closes the file
#detach()	Returns the separated raw stream from the buffer
#fileno()	Returns a number that represents the stream, from the operating system's perspective
#flush()	Flushes the internal buffer
#isatty()	Returns whether the file stream is interactive or not
#read()	Returns the file content
#readable()	Returns whether the file stream can be read or not
#readline()	Returns one line from the file
#readlines()	Returns a list of lines from the file
#seek()	Change the file position
#seekable()	Returns whether the file allows us to change the file position
#tell()	Returns the current file position
#truncate()	Resizes the file to a specified size
#writable()	Returns whether the file can be written to or not
#write()	Writes the specified string to the file
#writelines()	Writes a list of strings to the file


#1. File Reading Methods

with open("demofile.txt","r") as f:
    content = f.read()
    print(content)

with open("demofile.txt","r") as f:
    line1=f.readline()
    print(line1)

with open("demofile.txt","r") as f:
    lines=f.readlines()
    print(lines)


#2. File Writing & Modifying Methods

#with open("demofile.txt","a") as f:
#    f.write("\nFourth line.")

#lines_to_add =["\nLine A\n", "Line B\n"]

#with open("demofile.txt","a") as f:
#    f.writelines(lines_to_add)


#with open("demofile.txt", "a") as f:
 #   f.write("\nInstant save line.")
 #   f.flush()

 # Mode "a+" allows both writing and reading without wiping the file on open
with open("demofile.txt", "a+") as f:
    f.truncate(10)  # Truncates the file so only the first 10 bytes remain

