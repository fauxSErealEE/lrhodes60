#old_macdonald.py

def sing(animal, sound):
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
    print("And on that farm he had a",animal+",", "Ee-igh, Ee-igh, Oh!")
    print("With a",sound+",",sound,"here and a",sound+",",sound,"there.")
    print("Here a",sound+",","there a",sound+",","everywhere a",sound+",", sound+".")
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
    print()

def main():
    sing("cow", "moo")
    sing("duck","quack")
    sing("horse","neigh")
main()