# Day 1

#   installation
#       slack,git, github, vscode,assignment docs
#   python
#       download python (checked all)
#       version check  (python --version) or (python -V)
#   jupyter
#       install anaconda
#       start jupyter (jupyter notebook)
#   overview
#       python=> git=> 
#       pandas => numpy => matplotlib => seaborn
#       machine learning 
#             supervised , unsupervised learing 
#       problem 
#             supervised
#                   classification 
#                       email spam or not
#                       heart disease
#                    regression 
#                       house price prediction
#                       salary prediction
#
#                       
#             unsupervised (clustring)
#                   photo grouping,product recommendation
#        deep learning
#             ANN, CNN, RNN(LSTM,GRU)
#             ANN
#                   used for tabular data
#             CNN 
#                   used for images 
#             RNN(LSTM,GRU) 
#                   used for sequence data, (text data)
#                   used for text classificatin, 
#                   sentimental analysis
#             Backend 
#                   flask

#       vscode extension
#       python(microsoft), pylance(microsoft) jupyter

       
# Day 2
# printing
# 	print("hello")
# 	print("hello1","hello2", "hello3",1)

# running 
# 	python path or use play buttons

# semicolon
# 	no need of semi colin in python

# escape sequence 
# 	next line   \n   (backslash )
# 	tab         \t   

# variable 
# 	name="nitan"
# 	age=31
# 	rules for variable
# 		can use uppercase, lower case, number
#       first letter shoudl not be number
# 		can not use special character except _   (note we cant use $ unlink js)
# 		use snake case ...
# 		can't use keyword for variable name
# 	assigning multiple value 
# 	a,b=1,2   

# type 
# 	integer 1,2, -2 
# 	string  "nitan", 'nitan', '''nitan'''       (single quotes,double quotes, triple quotes)
# 	float   2.21,
# 	boolean True, False  (here first letter is capital, case sensitive)
# 	None      a=None  meaning  a is empty
# 	finding types => type(name) 


# comment 
# 	#   (ctr+/)
# 	"""...."""   (alt+shift+a)


# operator
# arithmetic
# 	+, -, * / % , ** 
# 	/  => o/p will always in float
#   //=> it give  closest integer value using floor
# 		print(12//5)  => 2.4 => 2
# 		print(-12//5)  =>-2.4 => -3
# comparision operator
# 	==, !=, > < >=, <=
# assignment operators 
# 	=, +=, -=, /= %=, **=
# logical operator
# 	not , and , or
# 	and => True if all are True
# 	or => True if one is True
# 	precidence not> and> or
# 		not True and False or True => (False and False or True)  => (False or True) => True


# operator 
# 	+ 
# 		 1+1=2  (number , numbr)
# 		"1"+"1"="11"  (string, string)
# 		"1"+1 => invalid  (number string invalid)
# 		[1,2,3]+[4,5,6] => [1,2,3,4,5,6]
# 	*
# 		1*1  = 1  (numbr, number)
# 		"a"*2 = "aa" (string* number) (not much imp)
# 		"1"*"1" = string * string is invalid

# int and float rule
# 	int and float arithmetic result float
# 		1*2.0 = 2.0
# 		1+2.0 = 3.0 ..
# 	when two int are divided it result float
# 		1/1 = 1.0


# round function
# 	print(round(1.23456,4))#1.2346
# 	print(round(1.23456,2))#1.23





# type conversion 
# 	conversion  (implicit) guess automatically 
# 		2+4.0 = 6.0 
	
# 	casting  (explicit)
# 		int(2.6),  => 2  it gives integer part (note it does gives nearest integer part)
# 		int(2.3)  => 2    gives integer part
# 		int("2")  => 2
# 		int("2.3") = it thow and error  (int cant convert float string)
# 		float(2) , float("2.3") => 2.3 => float can convert stringt to float
# 		str(2) => 2
# 		str(2.0)=> 2.0






# input 
# name = input("name :")
# 	every data in input is string so to convert it number user
# name  = int(input("name: ")   or
# name = float(input("name: ")




# Question 
# 	Write a program  to input 2 marks and print there sum
# 	write a program  to input side of a square and print its area
# 	write a program to input 2 floating point number and print their average
	



# Strings   (Strings in Python are immutable)
# 	can be defined by using ', " , ''', """
# 	cant use single quotes inside ' and so on 
# 	string formating 
# 		print(f"my name is {name} and surnam is {surname}")  #don't forget to place f

# 	index 
# 		name = "nitan" 0,1,2,3,4 or -5,-4,-3,-2,-1
# 			name[4]=> "n"   name[-1] ="n"
# 			name[1] => "i"
# 		string index does not support item assignment
# 		 ie name[0]="h"  (it is not valid)


#         # other method
#         fullname = "my name is nitan thapa"
#         print(fullname.upper())#MY NAME IS NITAN THAPA
#         print(fullname.lower())#my name is nitan thapa
# 		print(fullname.strip())#remove all left and right space
#         print(fullname.capitalize())#"My name is nitan thapa"
#         print(fullname.title())#My Name Is Nitan Thapa
#         print(fullname.startswith("m"))#True
#         print(fullname.endswith("m"))#False

#         print(fullname.replace("n","r"))#my rame is ritar thapa  (convert all n with 4)
#         print(fullname.count("n"))# 3  it count the total n
#         print(fullname.find("n"))#3  gives index of first n
#         print(fullname.find("z"))#-1  (if it does not find andy it return -1)
# 		  
#          print(len(fullname)) #it gives length of string





# question 
# 	WAP to input user's firt name and print its length
# 	WAP to find the occurance of " " in a string


# if  elif else	
# 	indendation is important , one indendation = 4space or one tab
# 	no cumpultion for else
# 	if(condition):
# 		statemen1
# 		statemnet2
# 	elif(condition):
# 		...
# 		..
# 	else:
# 		..
# 	eg 
# 		traffice light red-> stop, green -> go => yellow -> watch , else => invalid light
# 		range     90-100-> grade A , 80-89 => grade B , 70-79 -> C  else D
#       if daya is sunday or saturday => weekend else working day
# 		age>=18  => can vote else can not vote
# 		check if a number entered by the user is odd or even
# 		check if a number is a multiple of 7 or not 
#       lod example (for nested if)
# 		find the gretest of 3 numbers entered by the user 
# 			val1,val2,val3=2,4,1
# 			if(val1>=val2 and val1>=val3):
#     				print(val1)
# 			elif(val2>=val1 and val2>=val3):
#     				print(val2)
# 			else:
#     				print(val3)



#pass 
    #we can not have empty block in python 
    #if we want to have empty block we can use pass keyword

# a = 3
# if(a==2):
#     pass
# else:
#     print("a is not 2")
    







# Day 2

# Day 3

# Day 4

# Day 5

# Day 6

# Day 7

# Day 8

# Day 9

# Day 10

# Day 11

# Day 12

# Day 13

# Day 14

# Day 15