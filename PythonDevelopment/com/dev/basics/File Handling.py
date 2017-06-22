#File handling basics
#Opeing file needs permission like w(write),r(read),a(append),r+(read write)

file = open("hello.txt","a")
file.write("hello i am helloworld")
print(file)
file.close()