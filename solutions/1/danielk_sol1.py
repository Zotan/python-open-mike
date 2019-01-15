def reverse_list1(L):
    return L[::-1]


def reverse_list2(L):
    return [L[i-1] for i in range(len(L),0,-1)]


def reverse_list3(L):
    R = [None]*len(L)
    for i in range(len(L)):
        R[len(L)-1-i] = L[i]
    return R


def reverse_words1(S):
    return ' '.join(reverse_list1(S.split(' ')))

def reverse_words2(S):
    words = S.split(' ')
    R = ''
    for i in range(len(words),0,-1):
        R += words[i-1]
        if i > 1:
            R += ' '
    return R

def combine_dict(d1,d2):
    d3 = d2.copy()
    for key,val in d1.items():
        if key in d2:
            d3[key] = [d1[key], d2[key]]
        else:
            d3[key] = val
    return d3


def print_fun_lst(function_list, data):
    template = '''
{}:
INPUT: {}
OUTPUT: {}
---------------------------
'''
    for fun in function_list:
        print(template.format(fun.__name__, data, fun(*data)))


if __name__ == '__main__':

    my_list = [1,2,3,4]
    reversed_list = [4,3,2,1]
    my_string = 'hej hur är det?'
    reversed_string = 'det? är hur hej'
    my_dict1 = {'a': 3, 'b': ['x','y','z']}
    my_dict2 = {'c': 'this is a string', 'b': [3,2,1]}

    my_dict_1and2 = {'a': 3, 'b': [['x','y','z'],[3,2,1]], 'c': 'this is a string'}

    #testing functions

    assert reverse_list1(my_list) == reversed_list
    assert reverse_list2(my_list) == reversed_list
    assert reverse_list3(my_list) == reversed_list

    assert reverse_words1(my_string) == reversed_string
    assert reverse_words2(my_string) == reversed_string

    assert combine_dict(my_dict1,my_dict2) == my_dict_1and2

    print_functions = True
    if print_functions:
        
        rev_list_funs = [reverse_list1, reverse_list2, reverse_list3]
        print_fun_lst(rev_list_funs, [my_list])

        rev_str_funs = [reverse_words1, reverse_words2]
        print_fun_lst(rev_str_funs, [my_string])

        comb_dict_funs = [combine_dict]
        print_fun_lst(comb_dict_funs, [my_dict1,my_dict2])