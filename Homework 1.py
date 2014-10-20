__author__ = 'Madeleine'


def menu():
    print("1. Employee's first name"+"\n"+"2. Employee's last name"+"\n"+"3. Employee's DOB"+"\n"+"4. Employee's SSN"+"\n"+"5. Employee's address"+"\n"+"6. Employee's city"+"\n"+"7. Employee's zip code"+"\n"+"8. Print employee information"+"\n"+"9. Quit")
    return input("Please choose an option: ").strip()

def firstname():
    global a
    a = input("Employee's first name: ").strip().title()
    return a

def lastname():
    global b
    b = input("Employee's last name: ").strip().title()
    return b

def DOB():
    global x
    c = input("Month: mm").strip()
    d = input("Day: dd").strip()
    e = input("Year: yyyy").strip()
    x = (c+"/"+d+"/"+e)
    return x

def SSN():
    global y
    f = input("xxx: ").strip()
    g = input("xx: ").strip()
    h = input("xxxx: ").strip()
    y = (f+"-"+g+"-"+h)
    return y

def Address():
    global z
    i = input("Street address number: ").strip()
    try:
        int(i)
    except: "Please enter a number"
    l = input("Street address name: ").strip().title()
    return i

def City():
    global j
    j = input("City: ").strip().title()
    return j

def ZipCode():
    global k
    k = input("Zip Code: #####").strip()
    return k

def PrintInfo():
    print(a+" "+b)
    print(x)
    print(y)
    print(z)
    print(j)
    print(k+'\n')

def GetOut():
    exit()


def fullmenu():
    while True:
        choice = menu()
        if choice == "1":
            firstname()
        elif choice == "2":
            lastname()
        elif choice == "3":
            DOB()
        elif choice == "4":
            SSN()
        elif choice == "5":
            Address()
        elif choice == "6":
            City()
        elif choice == "7":
            ZipCode()
        elif choice == "8":
            PrintInfo()
        elif choice == "9":
            GetOut()
        else:
            print("You're a complete idiot")
            menu()

fullmenu()
