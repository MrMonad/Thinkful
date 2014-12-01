type(x) # type of variable

#bool
#false == none, 0, empty


#string
'{0} is {1} message'.format('this', 'is')



# int, float, long - big numbers in scientific notation



#list
list = [1,2,3,4]

list.pop() #takes off last element
del list[0] #remove 1 in the list


#tuple
#immutable, meaning operations create a new list, not modify old one
#useful for mantaining structure, like coordinates
#lists are more flexible, but if you want structure then use tuple



#sets
{1,2,3}
set([1,2,3])
#list without order

x & y #intersection
x | y #union
x - y #difference




#dictionary
dicts.key()
dicts.values()

dicts.get('non-existant key') #won't return an error message, avoiding error messages






#python reads up-down, but control statements make it into a tree instead of linear 
for i in range(10):
	print 'filler'
else:
	print 'terminating message after loop is finished'
# same with while



?????
try:
	1/0
except DivisionError:
	print 'no dividing by zero'



#defaultdict
?????
import collections
numbers = [1,2,3,4,5,6]
defaultdict = numbers.defaultdict(int)



#csv seperators: , ; /t /n | 
with open('path' , 'rU') as localfilename: #U for universal newlines ???
	pass

	for line in localfilename
	#process
#now closed

inputFile = open('path', 'r+')
inputFile.close()

#python only points to the file, doesn't load the entire file into python

strip('|') # string into list, seperated by delimiter
rstrip() #gets rid of spaces on the right, or wtv input you enter


iteritems() #iterates through object, just like items() but different space/time vs. acessing tradeoff


#pandas and csv packages are smarter with csv delimiters (like if you had , in entries)


import csv

inputReader = csv.reader(inputFile) # automatically coverts lines into lists


import pandas as pd 

df = pd.read_csv('file/path')
df['column']
pd[0:10]

