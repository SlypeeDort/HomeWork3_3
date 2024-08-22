def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b = 25)
print_params(c = [1, 2, 3])
list_ = [1, 2, 3]
print_params()
print()

values_list = ["Еда", 54, 6.5]
values_dict ={'a': 3, 'b': False, 'c': 'Дом'}
values_list_2 = ['Сон', 1]
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2)