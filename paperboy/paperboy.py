class Paperboy:

    def __init__(self, name, experience, earnings):
        self.name = name
        self.experience = experience
        self.earnings = earnings

    def __str__(self):
        return f"My name is {self.name}. I have sold {self.experience} papers and earned ${self.earnings}."
    
    def quota(self):
        return 50 + (self.experience / 2)
            
    def deliver(self, start_address, end_address):
        unit_sold = abs(end_address - start_address)
        self.experience += unit_sold
        target = self.quota()
        if unit_sold < target:
            self.earnings += (unit_sold * 0.25) - 2
        elif unit_sold == target: 
            self.earnings += unit_sold * 0.25
        elif unit_sold > target:
            self.earnings += target * 0.25 + (unit_sold - target) * 0.50
        return self.earnings
                
    def report(self):
        return f"I'm {self.name}, I've delivered {self.experience} papers and  I've earned {self.earnings} so far!" 



tommyday1 = Paperboy('Tommy', 90, 30)


print(tommyday1.experience)
print(tommyday1.quota())
print(tommyday1.deliver(4, 700))
print(tommyday1.earnings)
print(tommyday1.report())
(tommyday1.deliver(10, 40))
print(tommyday1)
(tommyday1.deliver(100, 705))
print(tommyday1)
(tommyday1.deliver(1, -6))
print(tommyday1)



