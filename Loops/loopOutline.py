'''
This outline will help solidify concepts from the Variables lesson.
Fill in this outline as the instructor goes through the lesson.
'''

#1) Make a int variable called x set to 0. Make a while loop that prints 
#out x and increments it by one. Make the loop run while x is less than
#or equal to 20.
x = 0 
while(x <= 20):
    print(x)
    x = x + 1
#2) Make a int variable called x set to 0. Make a while loop that prints 
#out x and increments it by one. Add an if statement that breaks the loop
#if x equals 15. Make the loop run while x is less than 100.
x = 0 
while(x < 15):
    print(x)
    x = x + 1
    if(x == 15):
        break
    
while(x < 100):
    print(x)
#3) Make a int list with three items inside. Make a for loop that prints 
#out all the items.
a = [1,2,3]
for x in a:
    print(a)


#4) Make a string list with three items inside: "Michael", "Chris", "Nino". 
#Make a for loop that prints out all the items. Add an if statement that 
#breaks the loop if the item equals "Chris".
b = ["Michael","Chris","Nino"]
for x in b:
    print(b)
    if(x == "Chris"):
        break
    


#5) Make a while loop with a common SYNTAX error.
x = 9 
while(x = 9)
    print(x)



#6) Make a for loop with a common SYNTAX error.
x = [8,9,10]
for x in x 
    print(x)

