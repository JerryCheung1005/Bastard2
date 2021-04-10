while True:
    string1 = str(input("Enter one string: "))
    string2 = string1[::-1]
    if string1 == string2:
        print("Yes")
    else:
        print("No")

    choice = input("Again or not? [N for not] ")
    if choice == 'N':
        break