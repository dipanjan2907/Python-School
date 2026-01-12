n=int(input("Enter no. of day in a week: "))
match n:
    case 1:print("MONDAY")
    case 2:print("TUESDAY")
    case 3:print("WEDNESDAY")
    case 4:print("THURSDAY")
    case 5:print("FRIDAY")
    case 6:print("SATURDAY")
    case 7:print("SUNDAY")
    case _:print("NO SUCH DAY")

