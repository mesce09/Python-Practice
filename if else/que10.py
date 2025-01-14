#Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).
pets=["dog","cat"]
def getpet(pets):
    while True:
        pet=input("enter your pet(dog or cat) - ")
        pet=pet.lower()
        if pet in pets:
            petage=input("enter your pet age- ")
            if petage.isdigit():
                petage=int(petage)
                break
            else:
                print("invalid age")    
        else:
            print("invalid input")
        
        
    return pet,petage

def checkfood(pet,petage):
    food=""
    if pet == "dog":
        if petage>2:
            food="adult dog food"
        else:
            food="puppy food"
    else:
        if petage>5:
            food="senior cat food"
        else:
            food="small cat food"

    return food        
        

def main():
    pet,petage=getpet(pets)
    food=checkfood(pet,petage)
    print(f"food for your {petage} years old {pet} is {food}")

main()