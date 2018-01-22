"""
We have list of dictionaries. Problem is to find a dictionary which contains max number of keys.
"""

DICT_LIST = [
    {'a':1, 'b':2},
    {'a':-1, 'b':-2, 'c':-3, 'd':-4},
    {'a':10, 'b':30, 'c':40}
]


def xyz(dict_list):
    res = dict_list[0]
    for dic in dict_list:
        if len(dic.keys()) > len(res.keys()):
            res = dic

    return res 


def main():
    res = xyz(DICT_LIST)
    print(res) 
    return


if __name__ == '__main__':
    main()