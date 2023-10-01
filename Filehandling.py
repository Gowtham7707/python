'''
reading, writing, deleting,creating of the files is called file handling


open ------> open()

Read/write

close ------> close()



modes
-----------------------------
r - read
w - write (turncate)
a - append
r+ - read write
w+ - write read (turncate)

'''
# ---------------------<  read the file >-----------------------------------  
# s=open('calling_file_handling.txt',mode='r')
# print(s.read())
# s.close()

# ---------------------<  write the file >-----------------------------------
# s=open('calling_file_handling.txt',mode='w')
# s.write("   bye gowtham")
# s.close()


# ---------------------<  append the file >-----------------------------------
# s=open('calling_file_handling.txt',mode='a')
# s.write("   bye gowtham")
# s.close()

# ---------------------<  Read&write the file >-----------------------------------
# s=open('calling_file_handling.txt',mode='r+')
# print(s.read())
# s.write("   r+ read")
# s.close()


# ---------------------<  Write&Read the file >-----------------------------------
# read opeartion not work because the file pointer act as a write opeartion for that we need to use "seek"
s=open('calling_file_handling.txt',mode='w+')
s.write("   w+ read")
s.seek(0)
print(s.read())
s.close()