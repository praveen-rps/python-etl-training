

#1. open the file for reading
fp = open("d://sample.txt", "r")

#2. read the contents of the file
#content = fp.read()

#content = fp.read(10)

#content = fp.readline()

#3. print the contents to the console
#print(content)

content = fp.readlines()
for line in content:
    print(line)

#4 . close the file
fp.close()