import random
import csv
import pickle

##### Save the dictionary "Students" to file ###### <-- Very good intuition here! Each of your commented descriptions of what each function is doing should actually be written as a docstring between the def function_name(): and the function iteself.  The formatting is important because sometimes you want to print what the function does and there it is, in a format that is expected.  You can learn more about formatting your code by reading a bit about the Python styleguide (PEP8)
def save(): ### I recommend being more specific in your naming. For now, this makes perfect sense since it's the only fcn that saves, but what if the program grows or a new person (like me) is reading your code and wants to know what is being saved with minimual effort? What is your game grows and I don't want to remember as I am reading line 257 what the save function which is defined on line 10 or so does?  It's easier if you make it clear.
	output = open('math.pk1', 'wb')
	pickle.dump(students, output)
	output.close()

###### Define a function to add or subtract two numbers ######
def question(n):
	if (n == '1') or (n == '2'):
		add = True
		subtract = False
	elif (n == '3') or (n == '4'): # isn't the actual question below and this bit above something that should be fed into the question?  Is this a time for classes?
		add = False
		subtract = True

	if (n == '1') or (n == '3'):
		start = 0
		end = 9
	elif (n == '2') or (n == '4'):
		start = 10
		end = 99

	A = random.randint(start, end) # think if make more sense as a global or local variable
	B = random.randint(start, end)
### Convert tabs to spaces at the lower corner of your sublime window. Because there are no curly braces in Python, the easiest way to know how indented something is is with the spaces (http://stackoverflow.com/questions/13884499/what-is-python-whitespace-and-how-does-it-work)

   	print ""

	if add:
		print "   " + str(A) # is there some classier way of doing the printing of many lines in a block like that?
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

	ans = "hi!" # ans doesn't make any sense, is it a placeholder? is it just cute? maybe give it a comment if you want to keep it so it doesn't make any sense to a reader?
	while ans.isdigit() == False:
		ans = raw_input("What is your answer? ") # OH ans is renamed here. I see, the first ans is a test.  If it doesn't change, the user hasn't put in anything.  Maybe I should suggest this be removed and point person to information about testing.

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
	print "-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~"
	print "You choose " + quizzes[int(n)-1] + ". Try to get three in a row!"
	print "-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~"


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
	print "-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~"
	print "Progress Chart for " + name
	print "-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~"
	print ""
	i = 0
	while i < len(quizzes):
		print quizzes[i] + ":  \t" + score(i+1)
		i += 1
	print ""
	print "-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~"
	print "-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~"
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
quizzes = ["single digit addition",  ### I would recommend making your file more readable (300 lines is a lot!) by putting all of the functions you have associated with the quiz types and put them in a seperate file which you import at the top of this file.
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
	elif ans == "3": ## for future: what if the user wants to save at some point other than you have offered it?
		save()
		print "Your work has been saved"
		print ""
		break

# For trouble shooting. Will print the current student's information
	elif ans == "100": ## is this something teachers will know? will the student know? tell them in the game or in the readme!
		print students[name]





