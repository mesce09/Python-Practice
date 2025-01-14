def getscore():
    while True:
        score=input("enter the score: ")
        if score.isdigit():
            score=int(score)
            if score<101:
                break
            else:
                print("Invalid input")
        else:
            print("Invalid score")
    return score
#Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).
def checkgrade(score):
    grade=""
    if score>=90 and score<=100:
        grade="A"
    elif score>=80 and score<90:
        grade="B"
    elif score>=70 and score<80:
        grade="C"
    elif score>=60 and score<70:
        grade="D"
    else:
        grade="F"
    return grade

def main():
    score=getscore()
    grade=checkgrade(score)
    print(f"your grade is {grade} and your score is {score}")

main()
