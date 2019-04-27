list = [12,4,56,34,56,896,-34]
min1=list[0]
min2=list[0]
min3=list[0]

for i in range(1, len(list)):
    if list[i] < min1:
        min3 = min2
        min2 = min1
        min1 = list[i]
    elif list[i] < min2:
        min3 = min2
        min2 = list[i]
    elif list[i] < min3:
        min3 = list[i]
print(min1, min2, min3)
