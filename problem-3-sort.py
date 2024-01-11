
user = input('what are 10 numbers, separate with comma')
raw = user.split(',')
num = []

#putting input into integer list
for i in raw:
    num.append(i)

lowest = num[0]

for i in num:
    print(i)
    # if int(num[i]) < int(lowest):
    #     lowest = num[i]
    # for j in num:
    #     if num[j] < num[i]:
    #         num_1 = num[j]
    #         num_2 = num[i]

    #         num[i] = num_1
    #         num[j] = num_2
print(num)
print(lowest)