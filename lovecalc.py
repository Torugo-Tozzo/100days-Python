import random

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total1 = 0
total2 = 0

for i in range(len(name1 + name2)):
    if (name1 + name2)[i].upper() == 'T' or (name1 + name2)[i].upper() == 'R' or (name1 + name2)[i].upper() == 'U' or (name1 + name2)[i].upper() == 'E':
        total1 += 1

for i in range(len(name1 + name2)):
    if (name1 + name2)[i].upper() == 'L' or (name1 + name2)[i].upper() == 'O' or (name1 + name2)[i].upper() == 'V' or (name1 + name2)[i].upper() == 'E':
        total2 += 1

score = int(str(total1) + str(total2))

if(int(score) < 10 or int(score) > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif(int(score) < 50 and int(score) > 40):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

