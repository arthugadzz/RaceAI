import math


class Pilot():
    """ Represents the AI that plays RaceAI """

    def __init__(self, adn): 
        self.adn = adn
        self.fitness = None
        self.nbMove = 0
        self.nbCollisions = 0
        self.actions = ['U', 'D', 'L', 'R']
        self.previous_moves = [0, 0]
        


    def choose_next_move(self, car):
        """ Choose a new move based on its state.
        Return the movement choice of the snake (tuple) """
        
        self.nbMove += 1
        
        vision = [car.x, car.y, car.speed, car.angle, car.collision, car.progres, *self.previous_moves] # * permet de déplier la liste
    
        movesValues = self.adn.neural_network_forward(vision) 
        movesValues = movesValues.tolist()
        #print(movesValues)

        # Chooses the best move (the move with the highest value)
        choice = movesValues[0].index(max(movesValues[0]))
        
        # TODO à remplacer avec les moves > 80% ?
        # moves = []
        # for x in movesValues:
        #     if x > 0.8:
        #         moves.append(self.actions[movesValues.index(x)])

        self.previous_moves.append(choice)
        if len(self.previous_moves) > 2:
            self.previous_moves.pop(0)
            
        return self.actions[choice]



    def compute_fitness(self):
        
        self.fitness = self.progres ** 2 / self.nbCollisions
        return self.fitness
    
            
    def mate(self, other, mutationRate=0.01):
        """ Mate with another pilot to create a new pilot """
        newDna = self.dna.mix(other.dna, mutationRate)
        return Pilot(newDna)
    

    def reset_state(self):
        self.nbMove = 0
