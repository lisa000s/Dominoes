sum = 0
count = 0
while (True):
    number = input()
    if number == '.':
        break
    else:
        sum += int(number)
        count += 1
print()
print(sum / count)