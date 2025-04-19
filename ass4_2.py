file1=open('output.txt','w')
writing=file1.write(input("enter text to write to the file:"))
file1.close()
print("Data successfully written to output.txt.")
print("")

file1=open('output.txt','a')
appending=file1.write(input("Enter additional text to append:"))
file1.close()
print(("Data successfully appended."))
print("")

file1=open('output.txt','r')
reading=file1.readlines()
file1.close()
print("Final content of output.txt:")
for line in reading:
    print(line.strip())


