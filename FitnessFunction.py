class FitnessFunction:
    Key = []

    # set up Key with 0s, 1s
    def setKey(self, newKey):
        FitnessFunction.Key = [len(newKey)]
        FitnessFunction.Key = list(newKey)

    def get_fitness(self, Snake):
        fitness = 0;
        # loop through our Snakes scales and pitare them to our candidates
        for i in range(0, Snake.size(self) and len(FitnessFunction.Key)):
            if Snake.get_scale(self, i) == int(FitnessFunction.Key[i]):
                fitness += 1
        return fitness

    def getMaxFitness(self):
        maxFitness = len(FitnessFunction.Key)
        return maxFitness
