from pet import Pet

pet_name = input("Enter your pet's name: ")
my_pet = Pet(pet_name)

my_pet.get_status()

my_pet.eat()
my_pet.sleep()
my_pet.play()

my_pet.train("jump")
my_pet.train("play dead")
my_pet.show_tricks()

print("End and a Happy Coding!")


