# -*- encoding=utf-8 -*-
from entity.element import Line, Station


# 加载列车实际到站时长信息
def load_data():
    line_files = [
        'metro_1.txt',
        'metro_2.txt',
        'metro_3.txt',
        'metro_4.txt',
        'metro_5.txt',
        'metro_6.txt',
    ]
    lines, weights = {}, {}

    for line_name in line_files:
        lines[line_name] = []
        for data in open(f'data/{line_name}', 'r', encoding='utf8'):
            station, weight = data.rstrip().split(',')
            if station not in weights:
                weights[station] = int(weight)
            lines[line_name].append(station)

    return lines, weights


def create_metro_map(lines: dict, weights: dict):
    stations_dict, lines_dict = {}, {}
    for line_name, line_stations in lines.items():
        line = Line(line_name)

        # 初始化站点
        for station_name in line_stations:
            line.add_station(station_name)
            if station_name not in stations_dict:
                stations_dict[station_name] = Station(station_name)

        num = len(line_stations)

        # 初始化邻站乘车权重
        stations_dict[line_stations[0]].add_neighbor(line_stations[1], weights[line_stations[1]])
        stations_dict[line_stations[num-1]].add_neighbor(line_stations[num-2], weights[line_stations[num-2]])
        for i in range(1, num-1):
            left, curr, right = line_stations[i-1], line_stations[i], line_stations[i+1]
            stations_dict[curr].add_neighbor(left, cost=weights[left])
            stations_dict[curr].add_neighbor(right, cost=weights[right])

        lines_dict[line_name] = line

    return stations_dict, lines_dict
