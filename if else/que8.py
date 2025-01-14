#Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).
def getpass():
    password=input("enter your password - ")
    return password

def checkpass(password):
    plen=len(password)
    if plen>10:
        print("password strength strong")
    elif plen>=6 and plen<=10:
        print("password strength medium")
    else:
        print("Password weak")

def main():
    password=getpass()
    checkpass(password)

main()