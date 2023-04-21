# -*- encoding=utf-8 -*-


class Line:
    def __init__(self, name):
        super(Line, self).__init__()
        self.name = name
        self.stations = []

    def add_station(self, station):
        self.stations.append(station)

    def get_intersect_station(self, other_line):
        return set(self.stations) & set(other_line.stations)

    def intersect_with_line(self, other_line):
        return bool(self.get_intersect_station(other_line))

    def in_line(self, station):
        return station in self.stations


class Station:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        self.change = False

    def add_neighbor(self, station_name, cost):
        self.neighbors[station_name] = cost

    def get_neighbors(self):
        return self.neighbors.keys()

    def get_neighbor_cost(self, neighbor_name):
        return self.neighbors[neighbor_name]

    def exe_change(self):
        self.change = True
