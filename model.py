import pygame
import random
# when a key is pressed, train the model on all the data points


class LinearRegression:
    def __init__(self, numberOfInputs):
        self.weights = []
        self.bias = 0
        self.learning_rate = 0.05
        for i in range(numberOfInputs):
            self.weights.append(random.uniform(0, 1))

    def printWeights(self):
        for i in self.weights:
            print(i)

    # data is a list of numbers of lists, each of which has length numberOfInputs+1, because output is the last one
    def train(self, data):
        guess = 0
        if (len(data)-1!=len(self.weights)):
            print("INPUTS AND WEIGHTS ARE NOT THE SAME LENGTH")
            print(len(data)-1, len(self.weights))
            return
            
        for i in range(len(self.weights)):
            guess += self.weights[i]*data[i]
        guess += self.bias

        answerIndex = len(data)-1
        error = (data[answerIndex] - guess)
        for i in range(len(self.weights)):
            self.weights[i] += error * data[i] * self.learning_rate
        self.bias += error * self.learning_rate
        
    # exclude answer from inputs here
    def test(self, inputs):
        sum = 0
        for i in range(len(self.weights)):
            sum += self.weights[i]*inputs[i]
        return sum + self.bias


def map(input, minInput, maxInput, minOutput, maxOutput):
    output = minOutput + ((maxOutput - minOutput) / (maxInput - minInput)) * (input - minInput)
    return output

# Initialize pygame
pygame.init()

width = 600
height = 600
pygame.display.set_caption('Linear Regression Model (for one input)')
background_colour = (0, 0, 0)

# set the window
window = pygame.display.set_mode((width, height))
window.fill(background_colour)

pygame.display.flip()
running = True

mouse = pygame.mouse.get_pos()
left = False

data = []
positions = []

#Create the model
model = LinearRegression(1)

# animation loop
while running:
    
    pygame.event.get()
    # mouse list
    mouse = pygame.mouse.get_pos()
    # update screen
    pygame.display.flip()
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            left = mouse_presses[0]
            
            if left:
                x = map(mouse[0], 0, width, 0, 1)
                y = map(mouse[1], 0, height, 1, 0)
                data.append([x, y])
                positions.append((mouse[0], mouse[1]))
                # for point in data:
                #     # print("Point")
                #     model.train(point)
        # if event.type == pygame.KEYDOWN:
        #     for point in data:
        #         print("Point")
        #         model.train(point)
    
    for point in positions:
        pygame.draw.circle(window, (0, 0, 255), point, 5)
    for point in data:
        # print("Point")
        model.train(point)

    # For calculating end points on line then drawing it
    x1 = 0
    y1 = model.test([x1])
    x2 = 1 
    y2 = model.test([x2])

    actualX1 = map(x1, 0, 1, 0, width)
    actualY1 = map(y1, 0, 1, height, 0)
    actualX2 = map(x2, 0, 1, 0, width)
    actualY2 = map(y2, 0, 1, height, 0)
    pygame.draw.line(window,(0, 255, 0),(actualX1,actualY1),(actualX2,actualY2))