def getyear():
    while True:
        year=input("enter the year - ")
        if year.isdigit():
            year=int(year)
            break
        else:
            print("invalid input")
        
    return year

def checkleap(year):
    leap=False
    if (year%400==0) or (year%4==0 and year%100!=0):
        leap=True
    return leap
        

def main():
    year=getyear()
    isleap=checkleap(year)
    if isleap:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

main()