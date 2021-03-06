import random
import csv
import pickle

##### Save the dictionary "Students" to file ######
def save():
	output = open('math.pk1', 'wb')
	pickle.dump(students, output)
	output.close()

###### Define a function to add or subtract two numbers ######
def question(n):
	if (n == '1') or (n == '2'):
		add = True
		subtract = False
	elif (n == '3') or (n == '4'):
		add = False
		subtract = True

	if (n == '1') or (n == '3'):
		start = 0
		end = 9
	elif (n == '2') or (n == '4'):
		start = 10
		end = 99

	A = random.randint(start, end)
	B = random.randint(start, end)

 
   	print ""

	if add:
		print "   " + str(A)
		print " + " + str(B)
		print "------"
		print " = "
		print ""

	if subtract:
		print "   " + str(A+B)
		print " - " + str(B)
		print "------"
		print " = "
	
	print ""

	ans = "hi!"
	while ans.isdigit() == False:
		ans = raw_input("What is your answer? ")

	if add: correct = A+B
	else: correct = A
	
	if int(ans) == correct:
		return True
	else:
		print "Sorry, the correct answer is " + str(correct)
		return False
	
###### Quiz ######
def quiz(n):
	print "\033c"
	print "-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-"
	print "You choose " + quizzes[int(n)-1] + ". Try to get three in a row!"
	print "-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-"
	

	i = 0
	while i < 3:
		i += 1
		if question(n):
			if i == 3: 
				students[name][int(n)] = 1
				print ""
				print "CONGRATUALTIONS! You got three correct answers in a row!"
				print ""
				raw_input("Press ENTER to continue")
			elif i == 1: print "Good job! You got " + str(i) + " correct answer! Try another!"
			else: print "Good job! You got " + str(i) + " correct answers! Try another!"
		else:	
			print "That's okay. Let's try again!"
			raw_input("Press ENTER to continue")
			print "\033c"
			i = 0

###### Matching ######
def matching():
	words = ["addition", "subtraction", "multiplication", "division", "arthimetic", "digit"]
	definition = [	"The one-dimensional combination of two numbers",
			"Solving for the number that will combine to make the correct one-dimensional combination",
			"The two-dimensional combination of two numbers",
			"Solving for the number that will combine to make the correct two-dimensional combination",
			"The processes of addition, subtraction, multiplication, and division of numbers (not variables)",
			"Any of the numbers from 0 to 9." ]

	print "\033c"
	print "-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~"
	print "You choose vocabulary matching. Try to match the words!"
	print "-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~"
	print ""
	print " -------------------------------------------------------------"
	print " |                                                           |"
	print " |   1. addition     2. subtraction      3. multiplication	|"
	print " |                                                           |"
	print "	|   4. division	    5. arithmetic       6. digit            |"
	print "	|                                                           |"
	print "	-------------------------------------------------------------"
	print ""	

	i = 0
	mylist = []
	while i < 6:
		i += 1
		A = random.randint(1,6)
		while A in mylist:
			A = random.randint(1,6)
		mylist.append(A)
		ans = raw_input(str(i)  + ": " + definition[A-1] + "  ")
		if int(ans) == A:
			print "Good job!"
			print ""
		else:
			print "I'm sorry, the correct answer is " + words[A-1]
			print "Let's start over (Press ENTER to continue)"
			raw_input()
			print "\033c"
			print "-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~"
			print "You choose vocabulary matching. Try to match the words!"
			print "-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~"
			print ""
			print " -------------------------------------------------------------"
			print " |                                                           |"
			print " |   1. addition     2. subtraction      3. multiplication	|"
			print " |                                                           |"
			print "	|   4. division	    5. arithmetic       6. digit            |"
			print "	|                                                           |"
			print "	-------------------------------------------------------------"
			print ""
			i = 0
		mylist.append(A)
	print ""
	print "Fantastic Work! You got all six answers correct."
	print ""
	print "(Press ENTER to continue)"
	raw_input()
	students[name][5] = 1




###### Define a function to print progress ######
def checkProgress():
	print "\033c"
	print "-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-"
	print "Progress Chart for " + name
	print "-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-"
	print ""
	i = 0
	while i < len(quizzes):
		print quizzes[i] + ":  \t" + score(i+1)
		i += 1
	print ""
	print "-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-"
	print "-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-"
	print ""
	raw_input("(Press ENTER to continue)")

##### A Function to Translate 1s and 0s ####
def score(n):
	m = students[name][n]
	if m == 1:
		return "complete"
	else:
		return "in progress"

###### Start of the program itself ######

## List quizzes
quizzes = ["single digit addition",
			"double digit addition",
			"one digit subtraction",
			"two digit subtraction",
			"  vocabulary matching"	]

##  Retrieve the student's data
try:
	file = open('math.pk1', 'rb')
	students = pickle.load(file)
	file.close()
except:
	students = {}
	name = "Rebecca"
	students[name] = ["1234",0,0,0,0,0]
	output = open('math.pk1', 'wb')
	pickle.dump(students, output)
	output.close()

## Identify the student and check password
print "\033c"
print ""
print "-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-"
print ""
print "         Welcome to the Math-Pratice-Time!"
print ""
print "-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-"
print ""

name = raw_input("What is your name? ")


exist = 0
for key in students:
	if key == name:
		exist = 1
		print "Welcome back, " + name + "!"
		print "Please enter your password: "
		pwd = raw_input()
		check = 0 
		while check == 0:
			if pwd == students[name][0]:
				print "Thank you"
				check = 1
			else:
				print "I'm sorry, that is not correct. please try again."
				pwd = raw_input()
		break

if exist == 0:
	students[name] = [0,0,0,0,0,0]
	print "Nice to meet you, " + name + "."
	print "Please chose a password: "
	students[name][0] = raw_input()
	print "Thank you"

print ""


# MADEUP STUDENT (so I don't have to keep logging in every time)
# students = {}
# name = "Rebecca"
# students[name] = ["1234",0,0,0,0,0]



# MAIN MENU
k=1
while k:
	print "\033c"
	print ""
	print "*~*~*~*~*~*~*~*~*~*~*~*~* MAIN MENU *~*~*~*~*~*~*~*~*~*~*~*~*"
	print ""
	print "What would you like to do? (Chose a number)"
	print ""
	print "1: Check my Progress   2: Take a Quiz   3: Save and Exit"
	print ""
	ans = raw_input()

# CHECK PROGRESS
	if ans == "1": checkProgress()

# CHOOSE A QUIZ
	elif ans == "2":
		print "\033c"
		print ""
		print "*~*~*~*~*~*~*~*~*~*~*~*~* QUIZ MENU *~*~*~*~*~*~*~*~*~*~*~*~*"
		print ""
		print "What quiz would you like to take? (Choose a number)"
		for q in quizzes:
			print "  %s: %s" % (quizzes.index(q) + 1, q)
		print ""
		ans = raw_input()
		if int(ans) <= 4:
			quiz(ans)
		elif ans == '5':
			matching()

# SAVE AND EXIT
	elif ans == "3":
		save()
		print "Your work has been saved"
		print ""
		break

# For trouble shooting. Will print the current student's information 	
	elif ans == "100":
		print students[name]
	




