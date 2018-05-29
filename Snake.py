#
from FitnessFunction import FitnessFunction
import random


class Snake:
    def __init__(self):
        self.defaultSnakeLength = 64
        self.fitness = 0
        self.scales = [0] * self.defaultSnakeLength

    # scalerate random indiv
    def gen_Snake(self):
        for i in range(0, self.size()):
            scale = random.randint(0,1)
            self.scales[i] = scale

    def get_scale(self, index):
        return self.scales[index]

    def set_scale(self, index, value):
        self.scales[index] = value
        self.fitness = 0

    # pub methods
    def size(self):
       return len(self.scales)

    def get_fitness(self):
        if self.fitness == 0:
            self.fitness = FitnessFunction.get_fitness(self, Snake)
        return self.fitness

