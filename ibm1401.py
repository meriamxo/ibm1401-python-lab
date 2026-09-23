choice = ""

while choice != "0":

    print("\nIBM 1401 OPERATOR CONSOLE")
    print("=========================")
    print("1. Card reader check")
    print("2. Payroll batch run")
    print("3. Job time estimate")
    print("4. Core memory calculator")
    print("5. Two-digit date check")
    print("6. GCD (converted from FORTRAN)")
    print("7. Interest table (converted from FORTRAN)")
    print("0. Power down")

    choice = input("\nSelect: ")

    if choice == "1":

        record = input("Enter record: ")

        length = len(record)

        digits = 0
        letters = 0
        spaces = 0

        for ch in record:

            if ch.isdigit():
                digits = digits + 1

            elif ch.isalpha():
                letters = letters + 1

            elif ch == " ":
                spaces = spaces + 1

        if length == 80:
            print("Length:", length, "-> OK")

        elif length < 80:
            print("Length:", length, "-> SHORT, padded to 80")

        else:
            print("Length:", length, "-> OVERFLOW")
            print("Lost characters:", record[80:])

        print("Digits:", digits)
        print("Letters:", letters)
        print("Spaces:", spaces)

    elif choice == "2":
        employees = int(input("How many employees? "))

        total_hours = 0
        total_pay = 0

        print("\nPAYROLL RUN")
        print(f"{'NAME':<12}{'HOURS':>8}{'RATE':>10}{'PAY':>10}")

        for i in range(employees):

            name = input("\nName: ")
            hours = float(input("Hours: "))
            rate = float(input("Rate: "))

            if hours <= 40:
                pay = hours * rate

            else:
                normal_pay = 40 * rate
                overtime_hours = hours - 40
                overtime_pay = overtime_hours * rate * 1.5
                pay = normal_pay + overtime_pay

            print(f"{name:<12}{hours:>8.1f}{rate:>10.2f}{pay:>10.2f}")

            total_hours = total_hours + hours
            total_pay = total_pay + pay

        print("----------------------------------------")
        print(f"{'TOTAL':<12}{total_hours:>8.1f}{'':>10}{total_pay:>10.2f}")

    elif choice == "3":
        print("Option 3 selected")

    elif choice == "4":
        print("Option 4 selected")

    elif choice == "5":
        print("Option 5 selected")

    elif choice == "6":
        print("Option 6 selected")

    elif choice == "7":
        print("Option 7 selected")

    elif choice == "0":
        print("Powering down...")

    else:
        print("Invalid option")