'''

Download the file from the following URL to your computer : http://media.pearsoncmg.com/bc/bc_production/media_development/media_manager_ircd_cdroms/MM_readme.txt

Write a program to read the file and count the number of words in the file.



'''


#The path to the downloaded file
filePath = '/Users/gm456e/Desktop/MM_readme.txt'

#Create a new file object
file=open(filePath,"r+")

#Read the file content and store it in a variable
file_content = file.read()

#Split the text in file_content variable into a list of words . split() will create a list of words
words = file_content.split()

#Create a empty dict to hold word counts
wordcount={}

#Iterate over the words list
for word in words:

    #Check to see if the word is not in the wordcount dict
    if word not in wordcount:
        #If its not then make the value of the word 1
        wordcount[word] = 1
    else:
        #If the word already exist in the dict, increment the count by 1
        wordcount[word] += 1

#Print the wordcount dict
print wordcount