class Vertex(object):
    def __init__(self, idx, value):
        self.id = idx
        self.value = value
        self.neighbours = []
        self.messages = []
        self.superStep = 0


class Node(object):
    def __init__(self, a, b, value):
        self.vertA = a
        self.vertB = b
        self.value = value

