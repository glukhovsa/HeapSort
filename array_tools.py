import random

def make_simple_array(length, left_border, right_border):
    tmp_simple_arr = []
    for i in range(length):
        tmp_simple_arr.append(random.randint(left_border, right_border))
    return tmp_simple_arr

def print_simple_array(simple_array):
    out_file = open("simple_array_out.txt", "w")
    for element in simple_array:
        out_file.write(str(element))
        out_file.write('\n')
    out_file.close()
    print(simple_array)

def make_dict_array(length, left_border, right_border):
    tmp_dict_arr = {}
    for i in range(length):
        tmp_dict_arr[i] = random.randint(left_border, right_border)
    return tmp_dict_arr

def print_dict_array(dict_array):
    out_file = open("dict_array_out.txt", "w")
    for key in dict_array.keys():
        out_file.write(str(key))
        out_file.write(":")
        out_file.write(str(dict_array.get(key)))
        out_file.write('\n')
    out_file.close()
    print(dict_array)

def add_simple_element(simple_array, left_border, right_border):
    tmp_simple_arr = simple_array[:]
    tmp_simple_arr.append(random.randint(left_border, right_border))
    return tmp_simple_arr

def add_dict_element(dict_array, left_border, right_border):
    tmp_dict_arr = dict_array.copy()
    length = len(tmp_dict_arr)
    tmp_dict_arr[length] = random.randint(left_border, right_border)
    return tmp_dict_arr

def half_sort_simple_array(simple_array):
    length = len(simple_array)
    tmp_simple_arr = simple_array[:]
    for i in range(length//2):
        for j in range(i, length):
            if tmp_simple_arr[i] > tmp_simple_arr[j]:
                tmp_element = tmp_simple_arr[i]
                tmp_simple_arr[i] = tmp_simple_arr[j]
                tmp_simple_arr[j] = tmp_element
    return tmp_simple_arr

def half_sort_dict_array(dict_array):
    length = len(dict_array)
    tmp_dict_arr = dict_array.copy()
    for i in range(length//2):
        for j in range(i, length):
            if tmp_dict_arr[i] > tmp_dict_arr[j]:
                tmp_element = tmp_dict_arr[i]
                tmp_dict_arr[i] = tmp_dict_arr[j]
                tmp_dict_arr[j] = tmp_element
    return tmp_dict_arr

if __name__ == '__main__':
    simple_arr = make_simple_array(10, -10, 10)
    print_simple_array(simple_arr)
    dict_arr = make_dict_array(10, -10, 10)
    print_dict_array(dict_arr)
    simple_arr = add_simple_element(simple_arr, -10, 10)
    print_simple_array(simple_arr)
    dict_arr = add_dict_element(dict_arr, -10, 10)
    print_dict_array(dict_arr)
    simple_arr = half_sort_simple_array(simple_arr)
    print_simple_array(simple_arr)
    dict_arr = half_sort_dict_array(dict_arr)
    print_dict_array(dict_arr)

