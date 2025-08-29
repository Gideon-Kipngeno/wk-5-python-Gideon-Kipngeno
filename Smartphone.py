# Base class (parent)
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery
    
    def call(self, contact):
        print(f"{self.brand} {self.model} is calling {contact}...")
    
    def charge(self, amount):
        self.battery += amount
        if self.battery > 100:
            self.battery = 100
        print(f"{self.brand} {self.model} charged. Battery now at {self.battery}%")

# inheritance (Derived class (child))  
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        # Call parent constructor
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system

    # Polymorphism(method with new behavior)
    def call(self, contact):
        print(f"{self.brand} {self.model} makes a GAMER call to {contact}!")

    def play_game(self, game):
        if self.battery < 20:
            print("Battery too low to play!")
        else:
            print(f"Playing {game} on {self.brand} {self.model} with cooling system {self.cooling_system}")

# Testing
phone1 = Smartphone("Samsung", "Galaxy S24", "256GB", 50)
phone2 = GamingPhone("Asus", "ROG 7", "512GB", 80, "Liquid Cooling")

phone1.call("Alice")
phone1.charge(30)

phone2.call("Bob")
phone2.play_game("PUBG")
phone2.charge(50)
