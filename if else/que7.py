#Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.
coffesize=["small","medium","large","extra large"]
def getorder(coffesize):
    while True:
        coffee=input(f"choose your coffe size from {coffesize}: ")
        coffee=coffee.lower()
        if coffee in coffesize:
            break
        else:
            print("invalid coffee")
    return coffee



def main():
    order=getorder(coffesize)
    extrashot=input("Do want to add an extra shot, yes or no?: ")
    if extrashot=="yes":
        print(f"your order is {order} coffee with extrashot.")
    else:
        print(f"your order is {order} coffee.")

main()