import random
def getage():
    while True:
        age=input("enter your age: ")
        if age.isdigit():
            break
        else:
            print("Invalid input")
        
    age=int(age)
    return age
#Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.
def checkprice(age):
    price=12 if age >=18 else 8
    return price
def randomday():
    days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    return random.choice(days)

def checkday(day,price):
    if day =="wednesday":
        price-=2
    return price

def main():
    day=randomday()
    age=getage()
    price=checkprice(age)
    finalprice=checkday(day,price)
    print(f"today is {day} and your final price is ${finalprice}")


main()
