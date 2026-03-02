# f=open("C:\\Users\\LENOVO\Desktop\\PYTHON.py\\A.txt","r")
# print(f.readlines())
#print(f.read(20))
#f.write("hello preetam reddy\n how are you\n\r brother")
#print("good ")
#2.......................................................
# try:
#     f=open("C:\\Users\\LENOVO\Desktop\\PYTHON.py\\A.txt","r")
#     print(f.readline())
# except:
#     print("file not found error")
# else:
#     f.close()
#     print("file close s...")

#3..........................................................

# try:
#     with open("C:\\Users\\LENOVO\Desktop\\PYTHON.py\\A.txt")as f2:
#         with open("C:\\Users\\LENOVO\Desktop\\PYTHON.py\\B.txt","w")as f3:
#             for i in f2:
#                 f3.write(i)
# except:
#     print("file not found error:")
# else:
#     f3.close()
#     print("file closed...")

# 4........................................
with open("myfile.txt","r")as file:
    lines=file.readline()
    while lines:
        print(lines)
        lines=file.readline()

#5.............................................
# with open("C:\\Users\\LENOVO\Desktop\\PYTHON.py\\B.txt","w")as f:
#     f.write("hey im inside the file raed me and learn code")
# import os
# file_path="C:\\Users\\LENOVO\Desktop\\PYTHON.py\\B.txt"
# if os.path.exists(file_path):
    # print("file exists:........")
# else:
#     print("file not found")

#6..................................
# with open("C:\\Users\\LENOVO\Desktop\\PYTHON.py\\B.txt","r")as f:
#     for line in f:
#         print(line)

#7..................................
# with open("myfile.txt","r") as f:
#     print(type(f)) # cheak the type 
#     f.seek(9)      # skip the 9 letter from staring 
#     print(f.tell()) #its tell the position of char
#     data=f.read(5) #start from 10 char
#     print(data)

#8......................................
# with open("C:\\Users\\LENOVO\Desktop\\PYTHON.py\\A.txt","r")as file:
#     file.seek(2)               #//////its remove first 2 letter and go to next line
#     print(file.tell())
#     content=file.read(40)        ////#its read next line
#     print(content)

#9............................
# with open("C:\\Users\\LENOVO\Desktop\\PYTHON.py\\A.txt","r")as file:
#     file.write("hello preetam")
#     file.truncate(10)               /#its allow you only 10 char in ur file

# #10.............................

# with open("myfile.txt","r")as file:

#     cont=file.read()
# #     print(cont)

# with open("A.txt","r") as f:
#     f.seek(2)
#     print(f.tell())
#     words=f.read(5)
#     print(words)
