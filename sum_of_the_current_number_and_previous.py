# Print the sum of the current number and the previous number

def sum_of_numbers():
    prev_num = 0
    for i in range(1, 11):
        sum = prev_num + i
        print("Current Number:", i, "Previous Number:", prev_num, " Sum: ", sum)
        prev_num = i

sum_of_numbers()