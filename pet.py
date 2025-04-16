import random

class Pet:
    MOOD_EMOJIS = {
        "happy": "😄",
        "tired": "😴",
        "hungry": "🍽️",
        "excited": "🤩",
        "grumpy": "😾",
        "content": "😌"
    }

    def __init__(self, name, pet_type="dog"):
        self.name = name
        self.pet_type = pet_type
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        self.actions = {
            "dance": "💃 does a little happy dance!",
            "sing": "🎤 sings a funny tune!",
            "fetch": "🎾 fetches the ball with joy!",
            "nap": "🛏️ curls up and takes a quick nap."
        }

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} enjoys some food 🍖. Hunger is now {self.hunger}. {self.get_mood_emoji()}")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} takes a nap 💤. Energy is now {self.energy}. {self.get_mood_emoji()}")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} plays around 🎲! Happiness: {self.happiness}, Energy: {self.energy}, Hunger: {self.hunger} {self.get_mood_emoji()}")
        else:
            print(f"{self.name} is too tired to play 😓. Try sleeping!")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned how to {trick}! 🧠")
        else:
            print(f"{self.name} already knows how to {trick}! 🙃")

    def do_action(self, action):
        if action in self.actions:
            print(f"{self.name} {self.actions[action]}")
            self.happiness = min(10, self.happiness + 1)
        else:
            print(f"{self.name} doesn't know how to '{action}'. 🤔")

    def get_status(self):
        print(f"🐾 {self.name} the {self.pet_type.capitalize()} — Status Report")
        print(f"Hunger: {self.hunger}/10 | Energy: {self.energy}/10 | Happiness: {self.happiness}/10")
        print(f"Mood: {self.get_mood()} {self.get_mood_emoji()}")

    def get_mood(self):
        if self.hunger > 7:
            return "hungry"
        elif self.energy < 3:
            return "tired"
        elif self.happiness > 7:
            return "happy"
        elif self.happiness < 3:
            return "grumpy"
        else:
            return "content"

    def get_mood_emoji(self):
        return self.MOOD_EMOJIS[self.get_mood()]

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows: {', '.join(self.tricks)} 🎓")
        else:
            print(f"{self.name} hasn’t learned any tricks yet. 🤷")
