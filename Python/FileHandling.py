#read a file
# file= open("FileHandling.txt", "r")
#print(file.read())

#add to file
'''file=open("FileHandling.txt", "a")
file.write("Masroor")
file.close()

file=open("FileHandling.txt", "r")
print(file.read()) '''

#write mode
f=open("FileHandling.txt","w")
f.write("A new line")
f.close()

f=open("FileHandling.txt", "r")
print(f.read())

#Create a new text file
g=open("New.txt", "w")
g.write("This is a mew text file")
g.close()

g=open("New.txt","r")
print(g.read())