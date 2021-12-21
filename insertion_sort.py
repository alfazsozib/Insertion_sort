
num_list = [5,8,6,1,7,9]

for i in range(len(num_list)):
    x = (num_list[i])
    j = i - 1
    while j >=0 and x < num_list[j]:
        num_list[j+1] = num_list[j]
        j -= 1                                                                                                      
    num_list[j+1] = x
for i in range(len(num_list)):
    print(num_list[i])