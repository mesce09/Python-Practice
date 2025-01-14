#Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman
weatherlist=["sunny","rainy","snowy"]
def getweather(weatherlist):
    while True:
        weather=input("enter the weather: ")
        weather=weather.lower()
        if weather.isdigit():
            print("Invalid input")
        else:
            if weather in weatherlist:
                break
            else:
                print("invalid input")
    return weather

def checkactivity(weather):
    activity=""
    if weather=="sunny":
        activity="Go for a Walk"
    elif weather=="rainy":
        activity="Read a book"
    elif weather=="snowy":
            activity="Build a snowman"
    return activity


def main():
    weather=getweather(weatherlist)
    activity=checkactivity(weather)
    print(f"Today weather is {weather} and you should {activity}")

main()
