from FitnessFunction import FitnessFunction
from SnakeNest import Nest
from Algorithm import Algorithm
import random


class SnakeGA:
    def __init__(self):
        print("Main start")
        # set a candidate snake
        FitnessFunction.setKey(self, "1111000000000000000000000000000000000000000000000000000000001111")

        # create initial Nest
        myPop = Nest(50, True)

        # evolve out Nest until we reach an optimum
        gencount = 0
        while myPop.getFittest().get_fitness() < FitnessFunction.getMaxFitness(self):
            gencount += 1
            print("#" * 128)
            print("generation: ", gencount, " Fittest: ", myPop.getFittest().get_fitness())
            self.print_snake(myPop)
            print("_" * 128)
            myPop = Algorithm.evolve_pop(myPop)


        print("*" * 128)
        print("Snake found")
        print("generation: ", gencount)
        self.print_snake(myPop)
        print("*" * 128)

    def print_snake(self, myPop):
        str1 = ''
        print("Best Snake: ", str1.join(str(e) for e in myPop.getFittest().scales))
        m = [list(' ' * 64) for y in range(5)]
        l = 2
        for i in range(0, 64):
            m[l][i] = myPop.getFittest().scales[i]
            l += random.randint(~-(l < 1), l < 4)
        for j in m:
            print(*j)

simple = SnakeGA()
