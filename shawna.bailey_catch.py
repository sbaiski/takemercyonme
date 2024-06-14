import pygame, simplege, random

""" catch.py 
    slide and catch Demo

"""

class laundry(simplege.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("laundry.png")
        self.setSize(25, 25)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
        
    def reset(self):
        #move to top of screen
        self.y = 10
        
        #x is random 0 - screen width
        self.x = random.randint(0, self.screenWidth)
        
        #dy is random minSpeed to maxSpeed
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()


class basket(simplege.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("basket.png")
        self.setSize(50, 50)
        self.position = (320, 400)
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
            
class LblScore(simplege.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)
        
class LblTime(simplege.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time left: 10"
        self.center = (500, 30)
    
 
class Game(simplege.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("laundryroom.jpg")
        
        self.num_laundry = 10
        self.score = 0
        self.lblScore = LblScore()

        self.timer = simplege.Timer()
        self.timer.totalTime = 30
        self.lblTime = LblTime()
        
        self.basket = basket(self)
        
        self.laundry_objects = []
        for _ in range(self.num_laundry):
            self.laundry_objects.append(laundry(self))
            
        self.sprites = [self.basket, 
                        self.laundry_objects,
                        self.lblScore,
                        self.lblTime]

        
def process(self):
    for laundry in self.laundry_objects:  # Corrected attribute name
        if laundry.collidesWith(self.basket):
            laundry.reset()
            self.sndlaundry.play()
            self.score += 1
            self.lblScore.text = f"Score: {self.score}"
                
    self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
    if self.timer.getTimeLeft() < 0:
        print(f"Score: {self.score}")
        self.stop()

class Instructions(simplege.Scene):
    def __init__(self, prevScore):
        super().__init__()

        self.prevScore = prevScore

        self.setImage("laundryroom.jpg")
        self.response = "Quit"
        
        
        self.directions = simplege.MultiLabel()
        self.directions.textLines = [
        "You are trying to catch up on laundry", 
        "Move with left and right arrow keys.",
        "Catch as much laundry as you can",
        "in the time provided",
        "",
        "Good luck!"]
        
        self.directions.center = (320, 200)
        self.directions.size = (500, 250)
        
        self.btnPlay = simplege.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100, 400)
        
        self.btnQuit = simplege.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (540, 400)        
        
        self.lblScore = simplege.Label()
        self.lblScore.text = "Last score: 0"
        self.lblScore.center = (320, 400)
        
        self.lblScore.text = f"Last score: {self.prevScore}"

        
        self.sprites = [self.directions,
                        self.btnPlay,
                        self.btnQuit,
                        self.lblScore]
    
    def process(self):
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()
        
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()


def main():
    keepGoing = True
    lastScore = 0

    while keepGoing:
        instructions = Instructions(lastScore)
        instructions.start()
        
        if instructions.response == "Play":    
            game = Game() 
            game.start()
            lastScore = game.score
            
        else:
            keepGoing = False
            
if __name__ == "__main__":
    main()