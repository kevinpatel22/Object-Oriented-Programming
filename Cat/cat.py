class Cat: 
    def __init__(self, name, preferred_food, meal_time):
        self.name = name
        self.preferred_food = preferred_food
        self.meal_time = meal_time

    def __str__(self):
        return (f"My name is {self.name} and I like to eat {self.preferred_food} at around {self.eats_at()}")
    
    def eats_at(self):
        if self.meal_time < 12:
            return (f"{self.meal_time} AM")
        elif self.meal_time >= 12 and self.meal_time < 24:
            return f"{self.meal_time - 12} PM"
        else: 
            return(f"(Humans don't use this time format: {self.meal_time})")

    def meow(self):
        return (f"My name is {self.name} and I eat {self.preferred_food} at {self.eats_at()}")

cat1 = Cat('Jerry', 'Mouse', 11)
cat2 = Cat('Cherry', 'Oatmeal', 25)


print(cat1.meow())
print(cat2.meow())


print(cat1)
print(cat2)

