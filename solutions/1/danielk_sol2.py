import numpy as n
import revc

my_lst = n.arange(100, dtype='i')
my_ret = n.empty(my_lst.size, dtype='i')

print('my list:\n {}'.format(my_lst))

print('reverse_1:')
my_ret = revc.reverse1(my_lst)
print('{}'.format(my_ret))

print('my list:\n {}'.format(my_lst))

print('reverse_2:')
revc.reverse1(my_lst)
print('{}'.format(my_lst))