arr = [4, 4, 4, 3, 3, 3, 1]
newArr = []

for item in arr:
    # print(item)
    # print(arr.count(item))
    if item not in newArr:
        # print(item)
        newArr.append(item)

print(newArr)
