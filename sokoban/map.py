class Map:
    def __init__(self, width, height, data):
        if len(data) != width * height:
            raise ValueError()
        self.width = width
        self.height = height
        self.data = data

    def __getitem__(self, coordinates):
        x, y = coordinates
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            raise ValueError()
        return self.data[y * self.width + x]

    def accessible(self, x, y):
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return False
        else:
            return self.data[y * self.width + x]