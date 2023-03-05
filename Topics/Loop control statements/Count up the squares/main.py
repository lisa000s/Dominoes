sum_of_numbers = 0
sum_of_squares = 0
while True:
    number = input()
    if number == 0:
        print('0')
        break
    else:
        sum_of_squares += int(number)**2
        sum_of_numbers += int(number)
    if sum_of_numbers == 0:
        break
print(sum_of_squares)