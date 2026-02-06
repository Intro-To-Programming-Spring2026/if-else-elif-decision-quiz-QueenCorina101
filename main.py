# Mini Project – Decision Quiz
# Student Name: Corina Clark
# Topic: If / Elif / Else
# Goal: Create a quiz that gives different feedback based on the user's answer

print("Welcome to the Decision Quiz!")
print("Welcome to the Georgia Quiz!")

print("What's the capital of Georgia?")
answer = input("Enter your answer: ")

if answer == "Atlanta":
    print("Correct! Atlanta is the capital of Georgia.")
elif answer == "atlanta":
    print("You're close! Remember to capitalize the first letter.")
else:
    print("You are incorrect. Try again!")
