import random
level = 0
Category = {
    1 : "Freezing",
    2 : "Cold",
    3 : "Warm",
    4 : "Hot",
    5: "Boiling",
}

while True:
    try:
        bound = int(input("Level: "))
        if bound <= 0:
            raise ValueError
        break
    except ValueError:
        pass

number = random.randint(1, bound)

def GetTemp(d, b):
    percentage = (d / b) * 100
    if percentage == 0:
        return "Bingo" , 6
    elif percentage >= 0 and percentage <= 1:
        return "Boiling", 5
    elif percentage >= 1 and percentage <= 3:
        return "Hot", 4
    elif percentage >= 3 and percentage <= 7:
        return "Warm", 3
    elif percentage >= 7 and percentage <= 15:
        return "Cold", 2
    else:
        return "Freezing", 1

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            raise ValueError
        Cdistance = abs(number - guess)
        Pdistance = Cdistance
        Plevel = level
        temp, level = GetTemp(Cdistance, bound)

        while temp != "Bingo":
            if Plevel == level:
                if Cdistance < Pdistance:
                    print(f"Still {Category[level]} but Getting Warmer")
                elif Cdistance > Pdistance:
                    print(f"Still {Category[level]} but Getting Colder")
                else:
                    print("No change")
            else:
                print(temp)
            guess = int(input("Guess: "))
            if guess <= 0:
                raise ValueError
            Pdistance = Cdistance
            Cdistance = abs(number - guess)
            Plevel = level
            temp, level = GetTemp(Cdistance, bound)
        else:
            print(temp)
        break
    except ValueError:
        pass


