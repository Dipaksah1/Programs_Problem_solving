#import re module for providing support for regular expression
import re

#Making a regular expression for validating an email

expression='^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

#Define a function for Validating an Email

def check(email):

    #passing the regular expression and the string in search() method

    if (re.search(expression,email)):
        print(email)




print("Application for verifying and show valid email addresses")
print()
x=int(input("How many email you want to verify : "))
print("Enter",x,"email addresses:  ")

#making list to store email address
y=[]
    
for z in range(x):
    y.append(input())

print()
print("Valid Email Adderess are: ")
#calling function to check valid email address
for e in y:
    check(e)

input()


    
    
