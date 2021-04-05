#dateconvert3.py

def main():
    months = ["January", "February", "March", "April",
              "May", "June", "July", "August", "September",
              "October", "November", "December"]

    day, month, year = eval(input("Enter day, month, and year numbers:"))
    
    date1 = "{0}/{1}/{2}".format(month,day,year)
    date2 = "{0} {1},{2}".format(months[month-1],day,year)

    print("The date is", date1, "or", date2+".")
main()