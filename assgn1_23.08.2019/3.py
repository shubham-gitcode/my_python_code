# Program to check if the input year is a leap year or not


from configparser import SafeConfigParser

#reading input from config file
def read_input():
    global year

    parser = SafeConfigParser()
    parser.read('year.ini')
    year = int(parser.get('year_info', 'YEAR'))


# To get year (integer input) from the user
def check_leap():
    global year

    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))


#executing functions in sequence
def main():
    read_input()
    check_leap()


#starting of program

main()

#end of program
