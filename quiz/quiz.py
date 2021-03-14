'''
This program quizzes user on basic high school trivia.

@author: Araceli Negrete-Garcia
'''

score = 0

one = input("What is the power house of the cell? \n A) mitochondria \n B) nucleus \n C) ribosome \n Answer: ")
if(one.upper()=="A"):
    score = score + 1
    print("Correct")
else:
    print("Incorrect, the correct answer is A.")


two = input("How many states comprise the United States? \n A) 13 \n B) 45 \n C) 50 \n Answer:")
if(two.upper() == "C"):
    score = score + 1
    print("Correct")
else:
    print("Incorrect, the correct answer is C.")


three = input("In y=mx+b, what does the m stand for? \n A) slope \n B) output \n C)I don't understand math \n Answer:")
if(three.upper() == "A"):
    score = score + 1
    print("Correct")
else:
    print("Incorrect, the correct answer is A.")


four = input("In English a person, place or thing is called: \n A) verb \n B) adjective \n C) noun \n Answer:")
if(four.upper() == "C"):
    score = score + 1
    print("Correct")
else:
    print("Incorrect, the correct answer is C.")


p = score/4 * 100
print("You got a [p]%.")

