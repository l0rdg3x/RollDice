from random import randint


class Dice():
    """
    n_faces = Max number of faces
    """
    def __init__(self, n_faces):
        self.n_faces = n_faces

    def roll(self):
        return randint(1, self.n_faces)
