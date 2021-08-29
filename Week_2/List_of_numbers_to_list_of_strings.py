def convert_int_to_string (list_of_strings):
    return list(map(int, list_of_strings))

print(type(convert_int_to_string(range(10))[2]))