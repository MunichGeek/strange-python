class Dog():
    def __init__(self, age):
        self.age = age
        self.barks = True

spike = Dog(age=2)
pluto = Dog(age=10)

print(f"Spike has age {spike.age}, Pluto has age: {pluto.age}")
spike.color = "brown"

print(f"Spike: {vars(spike)}")
