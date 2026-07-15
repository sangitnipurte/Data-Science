num = int(input("Enter a number: "))

match num:
    case 1:
        print("You entered one")
    case 21:
        print("You entered twenty one")
    case 3:
        print("You won a reward")
    case _:
        print("better luck next time")           