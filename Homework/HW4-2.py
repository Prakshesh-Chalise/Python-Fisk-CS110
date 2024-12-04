# 0) Function name: add_one 
#
# Takes a num and returns that num plus one.
#
# Parameters:
#   num: the starting num
#
# Return:
#   the starting num + 1
#
# e.g. add_one(5) -> 6
#      add_one(-1) -> 0

def add_one(num):
    num = num + 1
    return num


# 1) Function name: is_even 
#
# Takes a num and returns whether or not it is even.
#
# Parameters:
#   num: the num to check
#
# Return:
#   True if the num is even, False otherwise
#
# e.g. is_even(3) -> False
#      is_even(32) -> True

def is_even(num):
    num = num % 2
    if num == 0:
        return True
    else:
       return False




# 2) Function name: triple 
#
# Takes a num and returns triple the value.
#
# Parameters:
#   num: the starting num
#
# Return:
#   a num that is triple the original num
#
# e.g. triple(3) -> 9
#      triple(-10) -> -30

def is_triple(num):
    num = num * 3  
    return num
  

# 3) Function name: halve 
#
# Takes an int and returns an int that has half the
# value of that int, rounded down.
#
# Parameters:
#   num: an int, the starting num
#
# Return:
#   an int that has half the value, rounded down
#
# e.g. halve(5) -> 2
#      halve(-50) -> -25

def halve(num):
    num = num // 2
    return num

# 4) Function name: greater 
#
# Takes two nums and returns the larger one.
#
# Parameters:
#   num_1: a num
#   num_2: a second_num
#
# Return:
#   whichever of the two nums was larger
#
# e.g. greater(-1, 10) -> 10
#      greater(5, 100) -> 100

def greater(num_1, num_2):
    if num_1 >= num_2:
        return num_1
    else:
        return num_2



# 5) Function name: collatz 
#
# Takes one num, a positive integer, and returns either:
# - If the num is even, num //// 2
# - If the num is odd, num * 3 + 1
#
# Parameters:
#   num: a positive int to perform the operation on
#
# Return:
#   an int that is either num //// 2 or num * 3 + 1
#
# e.g. collatz(6) -> 3
#      collatz(5) -> 16
#      collatz(2) -> 1

def collatz(num):       
    if is_even(num):
        num = halve(num)
        return num
    else:
        num = is_triple(num)
        num = add_one(num)
        return num

# 6) Function name: collatz_loop
#
# Takes one num, a positive integer and returns
# the num of times the `collatz` function (the
# function you wrote in part 5) is called until the
# return value is 1.
#
# Parameters:
#   num: a positive int to attempt to turn into 1
#
# Return:
#   an int representing the num of times `collatz`
#   had to be run to turn the starting num into 1
#
# e.g. collatz_loop(1) -> 0
#      collatz_loop(8) -> 3
#      collatz_loop(5) -> 5

def collatz_loop(num):
    loop_number = 0
    while num != 1:
        num = collatz(num)
        loop_number = loop_number + 1
    return loop_number




# 7) Function name: collatz_conjecture
#
# Takes one num, a positive integer. For
# every int between 1 and the given num, computes
# the num of loops needed to reach 1 (by calling
# the `collatz_loop` function). Returns the maximum
# num of loops needed to reach 1 for each of
# those nums.
#
# Parameters:
#   num: a positive int at which to stop checking
#
# Return:
#   an int representing the maximum num of times
#   `collatz` had to be run to turn any of the checked
#   nums into 1
#
# e.g. collatz_conjecture(2) -> 1
#      collatz_loop(1) -> 0 and collatz_loop(2) -> 1, and the
#      max is 2, so the return is 1.
#
#      collatz_conjecture(5) -> 7 
#      Of the nums 1-5, it takes 3 the longest to reach 1:
#      3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 which is 7 steps,
#      so the return is 7.
#
#      collatz_conjecture(10) -> 19
#      Of the nums 1-10, it takes 9 the longest and it takes
#      19 steps, so the return is 19.
def collatz_conjecture(num):
    y = 1
    mx = 0
    while y < num:
        if collatz_loop(y) > mx:
            mx = collatz_loop(y)
        y = y+1
    return mx


#     
 


# More about this here:
# https:////en.wikipedia.org//wiki//Collatz_conjecture