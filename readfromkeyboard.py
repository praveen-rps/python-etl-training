file_name = input("Enter the file name to write: ")
#1. open the file for reading

with open(file_name, "a") as fp:
    print("Enter lines to write to the file (type 'exit' to stop):")
    while True:
        line = input()
        if line.lower() == 'exit':
            break
        fp.write(line + "\n")
    print("Lines written to file")


    