import mesa
import numpy as np
from random import uniform


class Bacteria(mesa.Agent):
    def __init__(self, model, pos, id):
        super().__init__(model)
        self.id = id
        self.pos = pos

    def can_reproduce(self):
        min_dist = min(
            np.linalg.norm(self.pos - np.array(other.pos)) 
            for other in self.model.agents if other != self
        )
        if min_dist < self.model.min_distance_to_reproduce:
            return True
        return False
    
    def can_move(self):
        if any(
            np.linalg.norm(self.pos - other.pos) >= 2*self.model.min_distance_to_move
            for other in self.model.agents if other != self
        ):
            return True
        return False

    def move(self):
        angle = uniform(0, 2 * np.pi)
        delta = np.array([np.cos(angle), np.sin(angle)]) * self.model.move_distance
        new_pos = self.pos + delta
        
        new_pos = np.clip(new_pos, [0, 0], [self.model.width, self.model.height])
        self.pos = new_pos

    def action(self):
        if self.can_reproduce():
            self.model.create_bacteria()
        
        self.move()

class BacteriaColony(mesa.Model):
    def __init__(self, p, v):
        super().__init__()
        self.num_agents = p
        self.min_distance_to_reproduce = 1
        self.min_distance_to_move = 1
        self.move_distance = v
        self.width = 10
        self.height = 10
        
        for n in range(self.num_agents):
            a = Bacteria(self, np.random.uniform(0, self.width, 2), n)                       

    def create_bacteria(self):
        pos = np.random.uniform(0, self.move_distance, 2)
        new_bacteria = Bacteria(self, np.random.uniform(0, self.width, 2), self.num_agents+1)
        self.num_agents = self.num_agents + 1

    def step(self):
        """Advance the model by one step."""
        self.agents.do("action")


for p in [2, 3, 4]:
    for v in [0.5, 1, 1.5, 3]:
        print("#######################")
        print(f"p={p}, v={v}")
        starter_model = BacteriaColony(p, v)
        for step in range(15):
            print(f"{starter_model.num_agents}")
            starter_model.step()