def common_elements(list1, list2):
    new_list = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j] and list1[i] not in new_list:
                new_list.append(list1[i])
    return new_list


print(common_elements([1, 2, 3, 4], [2, 4, 6, 8])) # should print [2, 4]
print(common_elements([1, 2, 3, 4, 4, 4], [2, 4, 4, 6, 8])) # should print [2, 4]
print(common_elements([1, 2, 3, 4], [6, 8])) # should print []
print(common_elements([], [6, 8])) # should print []
print(common_elements([1, 2, 3, 4], [])) # should print []
