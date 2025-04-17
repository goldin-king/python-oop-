from pet import Dog
# Creating a pet
mellow = Dog("Mellow")

# Interact with the pet
mellow.get_status()
mellow.eat()
mellow.play()
mellow.sleep()
mellow.train("sit")
mellow.train("roll over")
mellow.train("fetch")
mellow.train("shake paw")

# Check Mellow's status
mellow.get_status()

# Show the tricks Mellow learnt
mellow.show_tricks()
