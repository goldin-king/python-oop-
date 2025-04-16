class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = self.get_valid_input("hunger")
        self.energy = self.get_valid_input("energy")
        self.happiness = self.get_valid_input("happiness")
        self.tricks = []

    def get_valid_input(self, attribute_name):
        while True:
            try:
                value = int(input(f"Enter {attribute_name} level for {self.name} (0 to 10): "))
                if 0 <= value <= 10:
                    return value
                else:
                    print("❌ Value must be between 0 and 10. Try again.")
            except ValueError:
                print("❌ Invalid input. Please enter a number between 0 and 10.")

    def eat(self):
        old_hunger = self.hunger
        old_happiness = self.happiness

        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

        print(f"\n{self.name} eats.")
        if self.hunger < old_hunger:
            print(f"Hunger reduced to {self.hunger}.")
        if self.happiness > old_happiness:
            print(f"Happiness increased to {self.happiness}.")

    def sleep(self):
        old_energy = self.energy
        self.energy = min(10, self.energy + 5)

        if self.energy > old_energy:
            print(f"\n💤 {self.name} slept and gained energy. Now at {self.energy}/10.")
        else:
            print(f"\n💤 {self.name} is already fully rested.")

    def play(self):
        if self.energy <= 0:
            print(f"\n😞 {self.name} is too tired to play.")
            return

        old_energy = self.energy
        old_happiness = self.happiness
        old_hunger = self.hunger

        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

        print(f"\n🎾 {self.name} plays.")
        if self.energy < old_energy:
            print(f"  ⚡ Energy decreased to {self.energy}.")
        if self.happiness > old_happiness:
            print(f"  😃 Happiness increased to {self.happiness}.")
        if self.hunger > old_hunger:
            print(f"  🍖 Hunger increased to {self.hunger}.")

    def get_status(self):
        print(f"\n📋 Status of {self.name}:")
        print(f"  Hunger: {self.hunger}/10")
        print(f"  Energy: {self.energy}/10")
        print(f"  Happiness: {self.happiness}/10\n")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"\n🧠 {self.name} learned a new trick: '{trick}'!")

    def show_tricks(self):
        print(f"\n🎓 {self.name}'s Tricks:")
        if not self.tricks:
            print("  No tricks learned yet.")
        else:
            for trick in self.tricks:
                print(f"  - {trick}")
