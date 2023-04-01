row = int(input("Enter The Row: "))
column = int(input("Enter The Column: "))

list1 = [int(x) for x in input().split()]

print("List in 1D array: ",list1)

twoD_array = []

for i in range(row):
    twoD_array.append([])
    for j in range(column):
        twoD_array[i].append(list1[column*i+j])

print("List in 2d Array: ",twoD_array)

for j in range(row):
    if j % 2 == 0:
        for i in range(column):
            print(twoD_array[j][i])
    else:
        i = row - 1
        while i > 0:
            print(twoD_array[j][i])
            i = i - 1 