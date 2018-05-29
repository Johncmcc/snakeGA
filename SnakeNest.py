from Snake import Snake


class Nest:
    Snakes = []

    # constructors
    # create Nest
    def __init__(self, popSize, initialise):
        self.Snakes = [Snake() for i in range(popSize)]
        for i in range(popSize):
            self.newSnake = Snake()
            self.newSnake.gen_Snake()
            self.saveSnake(i, self.newSnake)

    # getters
    def getSnake(self, index):
        return self.Snakes[index]

    def getFittest(self):
        fittest = self.Snakes[0]
        for i in range(0, Nest.size(self)):
            if fittest.get_fitness() <= self.getSnake(i).get_fitness():
                fittest = self.getSnake(i)
        return fittest

    # public methods
    # get size

    def size(self):
        return len(self.Snakes)

    def saveSnake(self, index, indiv):
        self.Snakes[index] = indiv
