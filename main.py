from pet import Pet

def main():
    my_pet = Pet("Luna", pet_type="dragon")

    my_pet.get_status()
    my_pet.play()
    my_pet.eat()
    my_pet.sleep()
    my_pet.train("fly")
    my_pet.train("breathe fire")
    my_pet.do_action("dance")
    my_pet.do_action("fetch")  # Custom action
    my_pet.show_tricks()
    my_pet.get_status()

if __name__ == "__main__":
    main()
