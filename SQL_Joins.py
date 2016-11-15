left = ["apple", "berry", "cherry", "cherry", "grape"]
right  = ["cherry", "apple", "pineapple"]
left_dict = {}
right_dict = {}

def make_left_dict(left):
    for index, item in enumerate(left):
        if item in left_dict:
            left_dict[item].append(index)
        else: 
            left_dict[item] = [index]

make_left_dict(left)



def make_right_dict(right):
    for index, item in enumerate(right):
        if item in right_dict:
            right_dict[item].append(index)
        else: 
            right_dict[item] = [index]

make_right_dict(right)



def right_join(left, right, left_dict, right_dict):
    right_results = []
    for index, item in enumerate(left):
        if item in right_dict:
            index_list = right_dict[item]
            for i in index_list:
                right_results.append([index, i])
        else:
            right_results.append([index, -1])

    print right_results


def left_join(left, right, left_dict, right_dict):
    left_results = []
    for index, item in enumerate(right):
        if item in left_dict:
            index_list = left_dict[item]
            for i in index_list:
                left_results.append([i, index])
        else:
            left_results.append([-1, index])

    print left_results


def inner_join(left, right, left_dict, right_dict):
    inner_results = []
    for index, item in enumerate(left):
        if item in right_dict:
            index_list = right_dict[item]
            for i in index_list:
                inner_results.append([index, i])
        else:
            continue

    print inner_results

right_join(left, right, left_dict, right_dict)
left_join(left, right, left_dict, right_dict)
inner_join(left, right, left_dict, right_dict)

