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

        cards = int(input("Cards: "))
        lines = int(input("Lines: "))
        start_hour = int(input("Start hour (24-hour clock): "))
        start_minute = int(input("Start minute: "))

        reading_minutes = cards / 800
        printing_minutes = lines / 600

        total_minutes = reading_minutes + printing_minutes
        total_seconds = int(total_minutes * 60)

        job_hours = total_seconds // 3600
        remaining_seconds = total_seconds - (job_hours * 3600)

        job_minutes = remaining_seconds // 60
        job_seconds = remaining_seconds - (job_minutes * 60)

        print(f"Reading: {reading_minutes:.1f} min")
        print(f"Printing: {printing_minutes:.1f} min")
        print(f"Total: {job_hours}:{job_minutes:02}:{job_seconds:02}")

        start_seconds = (start_hour * 3600) + (start_minute * 60)
        finish_seconds = start_seconds + total_seconds

        while finish_seconds >= 86400:
            finish_seconds = finish_seconds - 86400

        finish_hour = finish_seconds // 3600
        remaining_finish = finish_seconds - (finish_hour * 3600)

        finish_minute = remaining_finish // 60
        finish_second = remaining_finish - (finish_minute * 60)

        if start_hour < 8:
            available_minutes = (8 * 60) - ((start_hour * 60) + start_minute)

        else:
            available_minutes = (24 * 60) - ((start_hour * 60) + start_minute)
            available_minutes = available_minutes + (8 * 60)

        print(
        f"Finishes at {finish_hour:02}:{finish_minute:02}:{finish_second:02}",
        end=""
        )

        if total_minutes <= available_minutes:
            print(" -> ON TIME")
        else:
            print(" -> LATE. Morning shift will not be happy.")

    elif choice == "4":
        memory = int(input("Memory (characters): "))
        records = int(input("Records: "))
        characters_per_record = int(input("Characters per record: "))

        records_per_pass = memory // characters_per_record

        passes = records // records_per_pass

        if records % records_per_pass != 0:
            passes = passes + 1

        laptop_memory = 8000000000
        equivalent_machines = laptop_memory // memory

        print("Records per pass:", records_per_pass)
        print("Passes needed:", passes)
        print(
        f"An 8 GB laptop has the memory of "
        f"{equivalent_machines:,} of these machines."
        )

    elif choice == "5":
        date = input("Date (DD MM YY): ")day = int(date[0:2])
        month = int(date[3:5])
        short_year = int(date[6:8])

        if short_year <= 30:
            year = 2000 + short_year
        else:
            year = 1900 + short_year

        if year % 400 == 0:
            leap_year = True

        elif year % 100 == 0:
            leap_year = False

        elif year % 4 == 0:
            leap_year = True

        else:
            leap_year = False

        valid = True

        if month < 1 or month > 12:
            valid = False

        else:

            if month == 2:

                if leap_year:
                    max_days = 29
                else:
                    max_days = 28

            elif month == 4 or month == 6 or month == 9 or month == 11:
                max_days = 30

            else:
                max_days = 31

            if day < 1 or day > max_days:
                valid = False

        if valid:

            if leap_year:
                print(f"{day:02}/{month:02}/{year} -> VALID (leap year)")
            else:
                print(f"{day:02}/{month:02}/{year} -> VALID")

        else:
            print(f"{day:02}/{month:02}/{year} -> INVALID DATE")

    elif choice == "6":
        print("Option 6 selected")

    elif choice == "7":
        print("Option 7 selected")

    elif choice == "0":
        print("Powering down...")

    else:
        print("Invalid option")