def prime_number_checker(number_to_check):
    prime_number = True
    for number in range(2, number_to_check):
        if number_to_check % number == 0:
            prime_number = False
    return prime_number

number_to_check = int(input("Type the number you want to check if tis is a prime number: "))
if prime_number_checker(number_to_check) == True:
    print("It's a prime number.")
else:
    print("It's not a prime number.")