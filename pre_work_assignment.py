def hello_name(user_name):
    """Display a simple greeting to a user."""
    print("hello_" + user_name.upper() + "!")

hello_name('username')

def first_odds(num_1):
    """Print a list of odd numbers.""" 
    num_1 = 0 
    while num_1 < 100:
        num_1 += 1

        if num_1 % 2 == 0:
            continue
        print(num_1)

first_odds('num')

def max_num_in_list(a_list):
    """Return the max number of the list provided."""
    a_list = [3,6,9,18,36,72,144,288,476]
    for max_int in a_list:
        max_int = max(a_list)
        
    print(max_int)   

max_num_in_list('max_int')

def is_leap_year(a_year):
    """Return a true or false statement if given year is a leap year."""
    a_year = int(a_year)               
    if a_year % 4 == 0: 
        bool(True)
    else:
        bool(False)
    
    return bool(a_year)       
print(is_leap_year(2020))


def is_consecutive(a_list):
    """Return a True or False statement for if a list is consecutive or not."""
    return sorted(a_list) == list(range(min(a_list), max(a_list) + 1)) 
print(is_consecutive([1,2,3,4,5,]))













