# -*- encoding=utf-8 -*-
from tool.get_data import load_data, create_metro_map


if __name__ == '__main__':
    # lines, weights = load_data()
    stations_dict, lines_dict = create_metro_map(*(load_data()))
    for k, v in lines_dict.items():
        print(k, v)

    while 1:
        start = input('>>出发站:')
        end = input('>终点站:')
        