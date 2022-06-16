# creating number list using range method
def numbers(start, end, interval):
    return list(range(start, end, interval))


def get_valid_input(prompt):  # Invalid input error handling with while loop
    while True:
        try:
            # If the user gives an integer then it becomes True loop and it will break in the end "else: break" mentioned right!
            value = int(input(prompt))
        except ValueError:
            print("That was invalid input you dumbfuck! please enter a valid number.")
            continue  # This is the key to continue the loop if the user gives invalid input
        if value < 0:
            print("You can't enter a negative number.")
            continue
        else:
            break  # this is where loops ends if the user gives valid input.
    return value


# calling the function and putting a variable to it
start = get_valid_input("Please enter a starting number: ")
end = get_valid_input("Please enter a ending number: ")
interval = get_valid_input("Please enter a interval number: ")

number_list = numbers(start, end, interval)  # creating a list of numbers
print(number_list)
choosen_number = get_valid_input(
    "Please enter the number that you want to search: ")


def binary_search(number_list, choosen_number):
    low = 0  # all these low, mid, high are just indexes in the list.
    high = len(number_list) - 1
    mid = 0

    while low <= high:
        mid = high + low // 2
        # If the choosen_number is greater, ignore the left half
        if number_list[mid] < choosen_number:
            low = mid + 1
        # If the choosen_number is smaller, ignore the right half
        elif number_list[mid] > choosen_number:
            high = mid - 1
        # This means that the choosen_number is at middle
        else:
            return mid

    # if we reach here, then the element is not present
    return -1


result_i = binary_search(number_list, choosen_number)

if result_i != -1:
    print(f"Found! {choosen_number} is at {result_i} index in that list!")

else:
    print("Not Found!")
