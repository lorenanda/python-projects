def payments(bill, people):
    try:
        return round((bill / people), 2)
    except:
        print("An error occured with the payments calculation")


def tip(bill, percentage, people):
    try:
        return round(((bill * (percentage / 100.00)) / people), 2)
    except:
        print("An error occured with the tip calculation")
    


def main():
    print("How much is the bill ?")
    while True:
        try:
            total_bill = float(input())
            break
        except:
            print("")
            print("Must be a number value")
            print("")
    print("")

    print("How many people ?")
    while True:
        try:
            nr_people = int(input())
            break
        except:
            print("")
            print("Must be a number value")
            print("")
    print("")

    print("What Percentage of Tip ?")
    while True:
        try:
            percentage = int(input())
            break
        except:
            print("")
            print("Must be a number value")
            print("")

    print("")
    print("Calculating Payment...")

    bill_payment = payments(total_bill, nr_people)
    tip_payment = tip(total_bill, percentage, nr_people)
    total_payment = bill_payment + tip_payment
    
    print('Each Person pays $%s for the bill' % \
          str(bill_payment))
    print('Each Person pays $%s for the tip' % \
          str(tip_payment))
    print('Which means each person will pay a total of $%s' % \
          str(total_payment))

if __name__ == '__main__':
    main()