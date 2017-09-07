'''
Write a program to create a new file named 'newFile.txt' and write atleast 5 lines of text.

Read the 'newFile.txt' and copy the contents of the file into another file named 'copyOfnewFile.txt'


'''

#Create variables to hold the files name
filename = 'newFile.txt'
newFileName = 'copyOfnewFile.txt'

#Read the newFile.txt and save the contents into file_content variable and close connection
f = open(filename,'r')
file_content = f.read()
f.close()

print file_content

#Write  file_content to the new file copyOfnewFile.txt and close connection
f = open(newFileName,'w')
f.write(file_content)
f.close()
