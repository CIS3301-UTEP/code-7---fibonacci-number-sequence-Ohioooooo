def get_fibonacci_number(position):

    if position == 1:  # check positions through if statement. 
        return 1
    elif position == 2: 
        return 1
    return get_fibonacci_number(position - 1) + get_fibonacci_number(position - 2)  # recursion shoukd be used then. 

def get_fibonacci_number_sequence(number):
    
     = []



if __name__ == "__main__":
    print(get_fibonacci_number(6))