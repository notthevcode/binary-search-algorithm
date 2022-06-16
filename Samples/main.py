# Invalid input error handling with while loop
def get_valid_input(prompt):
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


while True:
    data = input("Please enter a loud message (must be all caps): ")
    if not data.isupper():
        print("Sorry, your response was not loud enough.")
        continue
    else:
        # we're happy with the value given.
        # we're ready to exit the loop.
        break

while True:
    data = input("Pick an answer from A to D:")
    if data.lower() not in ('a', 'b', 'c', 'd'):
        print("Not an appropriate choice.")
    else:
        break
