# Program to remove extra spaces from a string and compressed into one space

from configparser import SafeConfigParser

# reading input from cofig file
def input_string():
    global input_string
    global space_flag

    # flag to check if spaces have occured
    space_flag = False

    parser = SafeConfigParser()
    parser.read('string.ini')
    input_string = parser.get('string_info', 'Input')


# Performing operations to remove extra spaces
def output_string():
    global input_string
    global space_flag
    output_string = []

    for index in range(len(input_string)):
        if input_string[index] != ' ':
            if space_flag == True:
                if input_string[index] == '!' or input_string[index] =='.' or input_string[index] == '?' or input_string[index] == ',':
                    pass
                else:
                    output_string.append(' ')

                space_flag = False
            output_string.append(input_string[index])

        elif input_string[index-1] != ' ':
            space_flag = True

    print(''.join(output_string))


# Assembling the functions in a sequence
def main():
    input_string()
    output_string()


# start of program

main()

# end of program

