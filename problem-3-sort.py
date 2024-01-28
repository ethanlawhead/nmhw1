
user = input('what are 10 numbers, separate with comma')
raw = user.split(',')
num = []
new = []
sum = 0
mode_dic = {}
#putting input into integer list
for i in raw:
    num.append(i)


#sorting
for i in range(0, len(num)):
    for j in range(i +1 , len(num)):
        if int(num[i]) >= int(num[j]):
            num[i], num[j] = num[j] , num[i]
        
#mean
for i in num:
    sum = sum + int(i)
mean = sum/(len(num))

#median
median = num[len(num)//2]

#mode
for i in num:
    if i in mode_dic:
        mode_dic[i] = mode_dic[i] + 1
    else:
        mode_dic[i] = 0
        mode_dic[i] = mode_dic[i] + 1
mode = max(mode_dic, key = mode_dic.get)
if int(mode_dic[mode]) <= 1:
    mode = "n/a"



print("the sorted list is", num)
print ("The mean is" , mean)
print("The median is", median)
print("The mode is", mode)