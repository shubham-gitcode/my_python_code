# Program to create a file with date and write the data into file.
# Then read the data from that particular file


from datetime import date


# reading file name with current date taking input from user through console (only name)
def get_file_name():
    global file_name

    file_name = input("Enter file name : ") 
    file_name =  str(file_name) + " " + str(date.today()) + ".txt"


# writing data into the file created
def write_file_data():
    global file_name
    data = ''
    print("File Name -> " + str(file_name))

    # creating an file reference for performing operations
    print('\nEnter 1 if your writing is done......\n')
    try:
        with open(str(file_name), "w") as FILE:
            while True:
                data = input('Enter data into file -> ')
                if data == '1':
                    break
                # writing data into the file
                FILE.write(str(data))
                FILE.write('\n')
    
            # closing the file
            FILE.close()
    except:
        print('File not opened.')

# reading data from the file created
def read_file_data():
    global file_name

    # creating an file reference for performing operations
    print('\n\nData Read From file -> ' + str(file_name))
    try:
        with open(str(file_name), "r") as FILE:
            print(FILE.read())
    
        # closing the file
        FILE.close()
    except:
        print("File can't be opened")


# Assembling the functions in a sequence
def main():
    get_file_name()
    write_file_data()
    read_file_data()


# Start of program

main()

# End of Program

