def get_fibonacci_number(position):

    if position == 1:  # check positions through if statement. 
        return 1
    elif position == 2: 
        return 1
    return get_fibonacci_number(position - 1) + get_fibonacci_number(position - 2)  # recursion shoukd be used then. 

def get_fibonacci_number_sequence(number):
    
    stored_numbers = []
    for i in range(1, number + 1):  # Loop through numbers. 
        stored_numbers.append(get_fibonacci_number(i))
    return stored_numbers  # Changed this line to print a list rather than the numbers individually as what it looks like from tes_code.




if __name__ == "__main__":
    print(get_fibonacci_number(6))  # this prints number in the sequence in the position given by user.

    print(get_fibonacci_number_sequence(9))  # this prints the sequence 1 by 1. 