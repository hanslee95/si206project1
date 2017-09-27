import os
import filecmp
import csv
import operator
def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	lst = []
	info = {}
	f = open(file, 'r')
	#reads in the file
	s_reader = csv.reader(f)
	#creates a tuple of 4 so I can iterate over it
	s_tup = [ (first, last, email, standing, dob) for (first, last, email, standing, dob) in list(s_reader)[1:]]
	#iterate over tuple of four for each element in the list to create a dictionary and append to new list.
	for elements in s_tup:
		info = {"First": elements[0], "Last": elements[1], "Email": elements[2], "Class": elements[3], "DOB": elements[4]}
		lst.append(info)
	
	return lst	
	
    	


#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	#sort by first, last, or email becauseo f the x[col]
	newlst = sorted(data, key=lambda x: x[col]) 
	#getting the first and last name of the sorted list by col argument.
	first = newlst[0]["First"] 
	last = newlst[0]["Last"]
	return first + " " + last




#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	d = {}
	for elem in data:
		if elem["Class"] not in d:
			d[elem["Class"]] = 0
		d[elem["Class"]] += 1	
	#sorted in descending order, while converting the dictionary to a list of tuple key/value pairs.	
	lst_tup = sorted([(k,v) for k, v in d.items()], key=lambda x:x[1], reverse = True)	
	
	return lst_tup


# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	d = {}
	lst = []
	sub = []
	dob = " "
	#this loop is for putting the DOB's in a list on there own.
	for key in a:
		dob = key["DOB"]
		sub= dob.split("/")
		lst.append(sub)
	#this loop is to put the DOB lst in a dictionary and count the days.
	for elem in lst:
		if elem[1] not in d:
			d[elem[1]] = 0
		d[elem[1]] += 1
	sorted_d = sorted(d.items(), key= lambda x:x[1], reverse = True)	
	
	return int(sorted_d[0][0])	
	
			




# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	#divide to get average
	denom = len(a)
	#lst of the all the ages
	dob_lst = []
	age_lst= []

	#this loop is for putting the DOB's in a lst on there own.
	for key in a:
		dob = key["DOB"]
		sub= dob.split("/")
		dob_lst.append(sub)
	for year in dob_lst:
		age_lst.append(2017 - int(year[2]))
	#average age equation	
	ave_age = sum(age_lst)/denom	
	
	return int(ave_age)


	

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	lst = []
	#sort by first, last, or email becauseo f the x[col]
	newlst = sorted(a, key=lambda x: x[col]) 
	#Open and create a csv file with open().'w' indicates you're writing strings into the file.
	csv = open(fileName, 'w')
	for dic in newlst:
		#the syntax for the data
		row = dic["First"] + "," + dic["Last"] + "," + dic["Email"] + "\n" 
		#write the syntax for each element into the csv file
		csv.write(row)

	



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

