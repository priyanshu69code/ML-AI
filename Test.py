row = int(input("Enter The Row: "))
column = int(input("Enter The Column: "))

list1 = [i for i in range(1,(row * column) + 1)]

print("List in 1D array: ",list1)

twoD_array = []

for i in range(row):
    twoD_array.append([])
    for j in range(column):
        twoD_array[i].append(list1[column*i+j])

print("List in 2d Array: ",twoD_array)

for j in range(column):
    if j % 2 == 0:
        for i in range(row):
            print(twoD_array[i][j])
    else:
        i = row - 1
        while i >= 0:
            print(twoD_array[i][j])
            i -= 1