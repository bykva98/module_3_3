def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(3)
print_params('не строка', [1,2,3])
print_params(1,2,3)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['задача', 1, False]
values_dict = {'a': 9 , 'b': 1.34, 'c': 23}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [6, 'вопрос']
print_params(*values_list_2, 42)