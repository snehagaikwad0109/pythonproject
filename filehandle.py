try :
    a=open("sample.txt","r")
    a.read()
    a.close()
except FileNotFoundError:
   print("The file 'sample.txt' was not found.")
finally:
    a=open("sample.txt","r")
    b=a.read()
    print(b)
    a.close()
