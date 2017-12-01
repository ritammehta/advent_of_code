num = raw_input("Enter the number: ")
sum = 0
pos = 0
for x in num:
    if x == num[pos - 1]:
        sum += int(x)
    pos += 1
print(sum)
