##Creating a class
class Pet:
    def __init__(self,name):
        self.name = 'Mellow '
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self. tricks = [ ]
       
    def bark(self):
        print(f"{self.name} says: Woof woof! 🐾")

    def eat (self):
        self.hunger = max(0,self.hunger -2)
        self.happiness = min(10, self.happiness +2)
        print( f"{self.name} just ate some food!  🍖")
    
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} just took a nap. 💤")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} just finshed playing and she had fun! 🐾")
        else:
            print(f"{self.name} is too tired to play. 😩")

    def get_status(self):
        print(f"{self.name}'s Status ")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} learned a new trick: {trick}! 🐶🎉")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks:")
            for trick in self.tricks:
                print(f"{trick}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")
