import random
import copy
class Hat:
    def __init__(self, **kwargs) -> None:
        self.kwargs = kwargs
        self.contents = []
        for key, value in self.kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def get_list(self):
        return self.contents

    
    def draw(self, num_balls):
        while len(self.contents) >= num_balls:
            rand = random.sample(self.contents, k=num_balls)
            [self.contents.remove(i) for i in rand]
            return rand
        
        return self.contents

        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    lst_balls = []
    for key, value in expected_balls.items():
        for i in range(value):
            lst_balls.append(key)
    expected_result = 0
    for i in range(num_experiments):
        rand = random.sample(hat.get_list().copy(), k=num_balls_drawn)
        if all(item in lst_balls for item in rand):
            expected_result += 1
    return expected_result / num_experiments


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=4,
                  num_experiments=3000)

print(probability)