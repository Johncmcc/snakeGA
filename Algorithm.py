from SnakeNest import Nest
from Snake import Snake
import random


class Algorithm:
    global elitism
    global uniformRate
    global mutationRate
    global pitSize

    uniformRate = 0.5
    mutationRate = 0.015
    pitSize = 5
    elitism = True

    # Public methods
    # Evolve a Nest
    @staticmethod
    def evolve_pop(pop):
        new_pop = Nest(pop.size(), False)

        # keep best Snake
        if elitism:
            new_pop.saveSnake(0, pop.getFittest())

        # crossover Nest
        # account for elitism offset
        offset = 0
        if elitism:
            offset = 1

        # loop over Nest size and create new Snakes with crossover
        for i in range(offset, pop.size()):
            indiv1 = Algorithm.pit_selection(pop)
            indiv2 = Algorithm.pit_selection(pop)
            newSnake = Algorithm.crossover(indiv1, indiv2)
            new_pop.saveSnake(i, newSnake)

        # mutate Nest
        for i in range(offset, new_pop.size()):
            Algorithm.mutate(new_pop.getSnake(i))

        return new_pop

    @staticmethod
    def crossover(indiv1, indiv2):
        new_key = Snake()
        # loop through scales
        for i in range(0, indiv1.size()):
            # crossover
            if random.random() <= uniformRate:
                new_key.set_scale(i, indiv1.get_scale(i))
            else:
                new_key.set_scale(i, indiv2.get_scale(i))

        return new_key

    @staticmethod
    def mutate(indiv):
        for i in range(0, indiv.size()):
            if random.random() <= mutationRate:
                scale = random.randint(0,1)
                indiv.set_scale(i, scale)

    # create pit_fight for
    @staticmethod
    def pit_selection(pop):
        # create a pit_fight Nest
        pit_fight = Nest(pitSize, False)
        for i in range(0, pitSize):
            rand_id = random.randint(0, pop.size() - 1)
            pit_fight.saveSnake(i, pop.getSnake(rand_id))

        # get fittest
        fittest = pit_fight.getFittest()
        return fittest
