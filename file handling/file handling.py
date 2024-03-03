# syntax (to open any file) : open("file name",mode(r/w/a))
# r for reading ( default mode / cann't write or append / throw error if file doesn't exist ) 
   # : rt ( to open text file / rt is by default no need to write rt to open text file  ) / rb ( to open binary file , like : jpg , png , pdf , exe ) , 
# w for writing ( cann't read or append / create a new file if file doesn't exist ) ,  
# x for creating new text file ( throw error if file already exist )

#f = open("myfile.txt", "x")  # creating a file 
f = open("myfile.txt", "w")  # write mode 
f.write(" hello , good morning!! ")  # it will erase all content of file and rewrite this new statement
f.close()  # written string will be visible on file after clsing it.

with open("myfile.txt") as f:  # by using with we do not need to close the file / by default read mode
    str=f.read()
    print(str)

with open("myfile.txt","a") as f:  # append mode / add text at the end of the file. it does not remove any text from file like write mode
    f.write("my name is aayushi")



#f=open("marks.txt","x")
    
with open("marks.txt","w") as f:
    line=["56,87,54\n","43,54,65\n","76,87,54\n"]  # we have to add new line manually
    #      OR
    #for ln in line:
    #    f.write( ln + "\n" )
    f.writelines(line)


print("______readline and writeline______")
with open("marks.txt","r") as f:
    i = 0
    while True:
        i = i + 1
        str = f.readline()
        if not str:
            break
        m1 = int(str.split(",")[0]) 
        m2 = int(str.split(",")[1]) 
        m3 = int(str.split(",")[2]) 
        print(f" marks of student {i} in sub {i} : {m1} ")
        print(f" marks of student {i} in sub {i} : {m2} ")
        print(f" marks of student {i} in sub {i} : {m3}\n ")

# in readline() method The str variable contains a string representing the current line 
# str=readlines() ;It reads all lines from the file and stores them in a list named str.



print("______'seek , tell , truncate'______")
with open("myfile.txt") as f:
    f.seek(9)             # seek() function allows you to move the current position within a file to a specific point
    current_pos=f.tell()
    data=f.read(10)        # read the next 5 bytes from 9th pos
    print(current_pos,data,end=",") 

with open('myfile.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5)

with open('myfile.txt', 'r') as f:
  print(f.read())