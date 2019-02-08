class Field:
    def __init__(self, key):
        self.visible = (key != None)
        if key == None:
            self.accessible = False
            self.target = False
            self.image = None
        elif key == '#':
            self.accessible = False
            self.target = False
            self.image = 'wall'
        elif key == ' ' or key == '$' or key == '@':
            self.accessible = True
            self.target = False
            self.image = 'floor'
        elif key == '.' or key == '*' or key == '+':
            self.accessible = True
            self.target = True
            self.image = 'target'