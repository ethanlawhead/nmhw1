
user = input('what are 10 numbers, separate with comma')
raw = user.split(',')
num = []
new = []
sum = 0
mode = {}
#putting input into integer list
for i in raw:
    num.append(i)


#sorting
for i in range(0, len(num)):
    for j in range(i +1 , len(num)):
        if num[i] >= num[j]:
            num[i], num[j] = num[j] , num[i]
        
#mean
for i in num:
    sum = sum + int(i)
mean = sum/(len(num))

#median
median = num[len(num)//2]

#mode
for i in num:
    if i in mode:
        mode[i] = mode[i] + 1
    else:
        mode[i] = 0
        mode[i] = mode[i] + 1




print("the sorted list is", num)
print ("The mean is" , mean)
print("The median is", median)