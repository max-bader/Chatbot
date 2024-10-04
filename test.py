nested_dict = {'person1': {'name': 'John', 'age': 25}, 'person2': {'name': 'max', 'age': 19}}
print(nested_dict['person2']['name'])

nested_list = [[1,2,3],['a','b','c'],[True, False, True]]
print(nested_list[1][0])

nested_list[0][1] = 5
nested_list.append(6)
print(nested_list)

list = [1, 2, 3, 4, 5]
list[1:4] = [20, 30, 40]
print(list)

nums = [
    [1,2], 
    [3], 
    [4,5,6]
    ]

def nested_avg(list):
    new_list = []
    for i in list:
        total = 0
        for j in i:
            total += j
        print(len(i))
        avg = total / len(i)
        new_list.append(avg)
    return new_list

print(nested_avg(nums))
