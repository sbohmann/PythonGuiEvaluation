class Field:
    def __init__(self, key):
        self.visible = (key != None)
        if key == None or key == '#':
            self.accessible = False
            self.target = False
        elif key == ' ' or key == '$' or key == '@':
            self.accessible = True
            self.target = False
        elif key == '.' or key == '*':
            self.accessible = True
            self.target = True