#creating and reading a text file
f=open("demo.txt",'w')
f.write("File is created..")
f=open("demo.txt",'r')
print(f.read())
print("file creation and reading is done")
