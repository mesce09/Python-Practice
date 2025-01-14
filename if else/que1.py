def getage():
    while True:
        age=input("enter your age: ")
        if age.isdigit():
            break
        else:
            print("Invalid input")
        
    age=int(age)
    return age
#Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).
def checkage(age):
    if age<13:
        print("Child")
    elif age>=13 and age<=19:
        print("teenager")
    elif age>=20 and age <=59:
        print("Adult")
    else:
        print("senior")

def main():
    age=getage()
    checkage(age)

main()

