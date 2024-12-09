#1.Create a class representing smartphone
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_life = battery_life

    def make_call(self, number):
        print(f"Calling {number}...")

    def send_message(self, number, message):
        print(f"Sending '{message}' to {number}...")

    def browse_internet(self, website):
        print(f"Browsing {website}...")

# Creating a specific smartphone object
iphone14 = Smartphone("Apple", "iPhone 14", 128, 24)
iphone14.make_call("+254712345678")
iphone14.send_message("+254789012345", "Hello, World!")
iphone14.browse_internet("google.com")

#2.Add attributes and methods to bring the class to life!
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, gpu, ram):
        super().__init__(brand, model, storage, battery_life)
        self.gpu = gpu
        self.ram = ram

    def play_game(self, game_name):
        print(f"Playing {game_name}...")

# Creating a gaming phone object
redmagic8s = GamingPhone("Nubia", "Red Magic 8S Pro", 256, 6000, "Snapdragon 8 Gen 2", 16)
redmagic8s.make_call("+254712345678")  # Inherited from Smartphone
redmagic8s.play_game("Call of Duty: Mobile")

class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_life = battery_life

    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}")

    def send_message(self, number, message):
        print(f"Sending '{message}' to {number} from {self.brand} {self.model}")

class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, gpu, ram):
        super().__init__(brand, model, storage, battery_life)
        self.gpu = gpu
        self.ram = ram

    def play_game(self, game_name):
        print(f"Playing {game_name} on {self.brand} {self.model}")

# Creating objects with unique values
iphone14 = Smartphone("Apple", "iPhone 14", 128, 24)
redmagic8s = GamingPhone("Nubia", "Red Magic 8S Pro", 256, 6000, "Snapdragon 8 Gen 2", 16)

# Demonstrating polymorphism
for phone in [iphone14, redmagic8s]:
    phone.make_call("+254712345678")  # Both phones can make calls

# Demonstrating encapsulation
redmagic8s.play_game("Call of Duty: Mobile")  # This is specific to GamingPhone
#Activity 2: Polymorphism Challenge! 🎭
#Create a program that includes animals or vehicles with the same action (like move()). 
#However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).
class Animal:
    def move(self):
        pass  # Placeholder for specific move implementation

class Dog(Animal):
    def move(self):
        print("Running")

class Bird(Animal):
    def move(self):
        print("Flying")

class Fish(Animal):
    def move(self):
        print("Swimming")

# Create instances of different animals
dog = Dog()
bird = Bird()
fish = Fish()

# Polymorphic behavior: calling the same method on different objects
for animal in [dog, bird, fish]:
    animal.move()
