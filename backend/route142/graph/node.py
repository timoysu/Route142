from functools import total_ordering
import math

@total_ordering
class Node(object):

    def __init__(self, point, dpoint, parent=None, conn_id=None, g_value=0):
        self.id = point.id
        self.point = point
        self.h_value = math.sqrt(math.pow(point.lat-dpoint.lat, 2) 
            + math.pow(point.lon-dpoint.lon, 2))
        self.g_value = g_value
        self.parent = parent
        self.connection_id = conn_id

    def f_value(self):
        return self.h_value + self.g_value

    def __lt__(self, other):
        return self.f_value() < other.f_value()

    def __eq__(self, other):
        return self.f_value() == other.f_value()