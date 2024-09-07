age=int(input("Enter Age:"))
match age:
  case 17:
    print("Not Eligible")
  case _:
    print("Eligible")
    