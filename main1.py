# ==== variables and Data types ====

student_name = "omer" #str 
print(student_name) 

student_Id = 607  #int
print(student_Id)

student_marks = 78.1  #float
print(student_marks)

fail = False   #bool
print(fail)

  #=========  Operators ======= 
 
# Familiar operators 
a = 5
b = 3
print("Addition :",a + b)
print("Subtraction :",a - b)
print("Multiply:", a * b)
print("Divide :", a / b)
print("remainder :", a % b)
print("a^b :", a ** b )

#example
num1 = 12
num2 = 5.10
print(num1 - num2)

#example
name1 = "omer"
name2 =  "bilal"

print(name1 + " " + name2)

# Relational operators
a = 50
b = 20

print(a == b)           #False
print(a != b)           #True
print(a >= b)           #True
print(a > b)            #True
print(a <= b)           #False
print(a < b)            #False
  
# Assignment operators

#example 1: 
num = 5
# num = num + num 
num += 5
print(num)

#example 2:
num = 6
num *= 5
print(num)

#example 3:
num = 8
num -= 7
print(num)

#example 4:
num = 10
num **= 5
print(num)

# ===logical operators ===
  
# not operator

num1 = 50
num2 =40
print(not num1 > num2)   #False
print(not num1 < num2)   #True

# and , or operator

num1 = False
num2 = False
print("And Operator", num1  and  num2)                #Both conditions must be true
print("Or Operator", num1  or  num2)                  #True if one or both are true

#example 1:

user_age = int(input("Enter your age:"))
user_eye_test = input("Enter test passed? (yes/no):")

if user_eye_test not in ["yes" , "no"]:
    print("Wrong Input. Please enter 'yes' or 'no' ")
if user_age >= 18 :
    print("You are eligible to apply for a driving license.")
else:
    print("You are not eligible to apply for a driving license.")

#example 2:

student_marks = int(input("Enter your marks :"))

if(student_marks >= 90) :
  print("A")
elif (student_marks >= 80 and student_marks < 90) :
   print("B")
elif (student_marks >= 70 and student_marks < 80) :
    print("C")
else:
    print("D")

#example 3:

has_business_class_ticket = input("Do you have a business class ticket? (yes/no): ").lower() == "yes"
has_medical_need = input("Do you have a special medical need? (yes/no): ").lower() == "yes"
checkin_time_in_hours = int(input("How many hours before departure did you check in?: "))


if (has_business_class_ticket  or has_medical_need) and checkin_time_in_hours >= 2:
    print(" You are eligible for priority boarding!")
else:
    print(" You are not eligible for priority boarding.")

    
 #   ===== Data structure =====

# ====list /array [] ====      (ordered aur Mutable)

#example 1:

student_names = ["bilal","omer" ,"alishba","maha","areeba","ali","sara","hani"]   
number_one = student_names[0]
print(number_one)
number_two = student_names[4]
print(number_two)
number_three = student_names[6]
print(number_three)
number_four = student_names[2]
print(number_four)
print(student_names)
     
 #example 2: 

BirdsName = ["peacock","duck","eagle","owl","parrot" ,"crow"]
one =BirdsName[1]
print(one)
zero = BirdsName[0]
print(zero)
three = BirdsName[3]
print(three)
four = BirdsName[4]
print(four)
five = BirdsName[5]
print(five)
two = BirdsName[2]
print(two) 

#example 3: list methods

BirdsName = ["peacock","duck","eagle","owl","parrot" ,"crow"]       
BirdsName.append("seagull")                                                 #add one element at the end
print(BirdsName)

BirdsName = ["peacock","duck","eagle","owl","parrot" ,"crow"]            
print(len(BirdsName))          
                                                      
BirdsName = ["peacock","duck","eagle","owl","parrot" ,"crow"]             
print(BirdsName.sort())                                                     #sort in ascending order

subjects = ["math","Enlish","urdu", "chemistry","physics"]  
subjects.reverse()                                                          # reverse list
subjects.remove("urdu")                                                     #remove first occurrence of element
print(subjects)

subjects = ["math","Enlish","urdu", "chemistry","physics"]  
subjects.insert (4, "pst")                                                   #insert element at index
subjects.pop(1)                                                              #removes element at index
print(subjects)

subjects = ["math","Enlish","urdu", "chemistry","physics"]  
del subjects[3]                                                                      #delete element at index
print(subjects)


# ==== Dictionary /object  {} =====      (key-value pairs mutable)

#example 1:

user_name = {
   "name" : "ali anwar",         
    "age" :  20 ,
   "city" : "karachi"
}
print(user_name)

#example 2: {[{}]}

customer = {
       "name" : "omer anwar",
     "contact": 87643620,
       "item" : ["bags", "shoes","dresses","makeup"],
    "address" : {
                   "country" : "pakistan",
                      "city" :"karachi",
                       "area": "aiwan-e-sadar"
           }
}
print(customer)

# ====== Tuple ()  ======  (ordered aur immutable)

months_Name = ("january","february","march","april","may",)                               #no change   
# months_Name[3] = "june"                                                                  #error
print(months_Name)

tup = (1,4,6,9,0,4,6,5)                                                                   # no change
# tup [3] = 7                                                                             #error
print(tup)

# ==== Set ==== {}     (mutable)

fruit_Name = {"apple","banana","mango","cherry","apple","cherry"}                         #set of element  immutable
# fruit_Name[4]  ="orange"                                                                #error
print(fruit_Name)
print(len(fruit_Name))


# === Conditional statements ===

#example 1:
student_timing = 9
if (student_timing > 9):
    print("you are late")
    
elif (student_timing == 9):
    print("you are on time")
else:
    print("you are early bird")

#example 2:
username = "omer"
if(username == "zia"):
   print("wellcome sir")
elif(username == "saba"):
   print("wellcom mam")
else:
   print("invalid user")

#example 3:

age = 21 
if age == 18:
   print("eligiable for driving lisence")
elif age > 18:
   print("eligiable for driving lisence and vote")
else:
   print("not eligiable")
  

# if  statement nested   

#example 1:

shirt_Color = "green"
shirt_Color1 = "orange"

if shirt_Color == "green":   
     print("Green: The player  earned 5 points.")
     if  shirt_Color1 == "red":                                  #nesting
         print("Red: The player just earned 2.5 points.")
     elif shirt_Color1 == "orange":
         print("Orange: The player just earned 2.5 points.")
     else:
            print("No points")           

elif(shirt_Color == "yellow"):
     print("Yellow: The player  earned 4 points.")
    
elif(shirt_Color == "blue" ):
     print("Blue: The player  earned 6 points.")
    
else: 
     print("please select right color")

#example 2:     

name = "ali"
age = 10

if name == "sara" :
   print("welcome sara")
   if age >= 18 and age<= 60:                               #nesting
      print("you are still a user")
   elif age <18 :
      print("you are underaged")
   else:
      print("your are retired") 
elif name == "ali":
   print("welcome ali")  
   if age >= 18 and age<= 60:
      print("you are still a user")
   elif age <18 :
      print("you are underaged")
   else:
      print("your are retired") 
elif name == "zia": 
   print("welcome zia")
   if age >= 18 and age<= 60:
      print("you are still a user")
   elif age <18 :
      print("you are underaged")
   else:
      print("your are retired")                         
       
else:
    print("you are not user")

 # ==== Functions ====

#example 1:
def x():
    print("Hello")
    print("Happy Brithday to you!")
    
x()
x()
x()

#example 2:

def vegetable():             
    return   "ladyfinger:"          
name = vegetable()
print(name)
print(name)

#example 3:
def greet(student):
    print(f"{student}, welcom back to class")

greet("zia") 

#example 4:

def calculator(var1,var2, operation):
    if operation == "add":
        print(var1 + var2)
    elif operation == "subtract":
        print(var1 - var2)
    elif operation == "multiplication":
        print(var1 * var2)
    elif operation == "devide":
        print(var1 / var2)
    else:
        print("not defined")

check = calculator(1600, 10, "devide") 
check = calculator(7,8, "add")
check = calculator(8,4, "subtract")
check = calculator(6,4, "multiplication")

# == input method ==
#example 1:

name = input("what is your name :")   #input method
age = input("Enter your age :")
roll_number = input("Enter your rollnumber :")

#example 2:

marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance percentage: "))

if marks >= 40 and attendance >= 75:
    print("You have passed the exam. ")
else:
    print("You have failed the exam. ")

  
# === for loop method ===
#example 1:

fruits = ["apple","mango","orange","banana"]                #list
for names in fruits:                                        #for loop
    print(names)
    
#example 2:

animals = ["cat","dog","cow","horse","donkey"]
for names in animals :
    print(names)
else:
    print("The End!")

#example 3:

for i in range(3):   #method
     print(f"Hello World!")

for i in range(8):
     print(f"Hello world,{i+1}")     

  # ==== while loop ===

#example 1:
i = 25
while i >= 1:
    print(i)
    i -= 1
      
#example 2:

num = 1
while num <= 6:
     print("Number:", num)
     num +=1  

#example 3:

correct_password = "1234"
password = input("Enter password: ")

while password != correct_password:
    print("Wrong password, try again.")
    password = input("Enter password: ")

print("Access granted!")

#example 4:

secret_number = 7

while True:
    guess = int(input("Guess the number (1-10): "))
    
    if guess == secret_number:
        print("Correct! You guessed it right.")
        break                                                                # exit the loop
    else:
        print("Wrong guess. Try again.")
