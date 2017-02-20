
class RowUpdate(object):
    def __init__(self, line):
        self.x, self.y, self.z, self.new_value = map(int, line)


class RowQuery(object):

    def __init__(self, line):
        self.x1, self.y1, self.z1, self.x2, self.y2, self.z2 = map(int, line)
