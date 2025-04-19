try:
    file=open('sample.txt','r')
    print("Reading file content :")
    line_num=1
    for line in file:
        print("line",line_num,":",line.strip())
        line_num+= 1

    file.close()

except FileNotFoundError:
    print("Error: the file 'sample.txt' was not found")

