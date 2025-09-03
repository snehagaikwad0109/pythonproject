a=input("Enter data to write into the file :")
b=open("output.txt","w")
c=b.write(a)
print("Data added successfully")
b.close()

a=input("Enter additional text to append to the file :")
b=open("output.txt","a")
c=b.write('\n')
c=b.write(a)
print("Data successfully appended")
b.close()

print("Final contents of output file")
a=open("output.txt","r")
b=a.read()
print(b)
a.close()

