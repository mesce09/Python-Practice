ripcolor=["green","yellow","brown"]
#Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe
def getfruit():
    while True:
        fruit=input("enter the fruit: ")
        if fruit.isdigit():
            print("Invalid input")
        else:
            break
    return fruit

def checkripe(ripcolor):
    ripeness=""
    while True:
        color=input(f"choose from {ripcolor}: ")
        color=color.lower()
        if color in ripcolor:
            if color=="green":
                ripeness="Unripe"
                break
            elif color=="yellow":
                ripeness="Ripe"
                break        
            elif color=="brown":
                ripeness="Overripe"
                break
            else:
                print("invalid color")
        else:
            print("invalid color")
    
    return ripeness 


def main():
    fruit=getfruit()
    ripness=checkripe(ripcolor)
    print(f"your fruit is {fruit} and it is {ripness}")

main()
