# Print the sum of the current number and the previous number

def sum_of_numbers():
    numbers = list(range(1, 11))
    prev_num = 0
    for num in numbers:
        sum = prev_num + num
        print("Current Number:", num, "Previous Number:", prev_num, " Sum: ", sum)
        prev_num = num

sum_of_numbers()