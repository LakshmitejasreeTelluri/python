f=open('example.bin','wb')
f.write(b'this is binary file')
f=open('example.bin','rb')
print(f.read())
