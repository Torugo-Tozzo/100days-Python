# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total = 0
def wich_size(tam):
    global total
    if(tam == "S"):
        total += 15
    elif(tam == "M"):
        total += 20
    elif(tam == "L"):
        total += 25

wich_size(size)

def pepeornot(pepero):
    global total
    if(pepero == "Y"):
        if(size == "S"):
            total += 2
        else:
            total += 3

pepeornot(add_pepperoni)

def chesseornot(ychessn):
    global total
    if(ychessn == "Y"):
        total += 1

chesseornot(extra_cheese)

print(f"Your final bill is: ${total}.")