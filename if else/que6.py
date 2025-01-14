#Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

def getdistance():
    while True:
        distance=input("enter your distance: ")
        if distance.isdigit():
            break
        else:
            print("Invalid input")
        
    distance=int(distance)
    return distance
def checktrans(distance):
    transport="walk"
    if distance>=3 and distance<=15:
        transport="Bike"
    elif distance>15:
        transport="Car"
        
    return transport

def main():
    distance=getdistance()
    trans=checktrans(distance)
    print(f"distance is {distance} and transport should be {trans}")


main()
