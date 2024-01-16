
user = input('what are 10 numbers, separate with comma')
raw = user.split(',')
num = []
new = []
sum = 0
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




print("the sorted list is", num)
print ("The mean is" , mean)