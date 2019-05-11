class Player:
    
    def __init__(self, gold_coins = 0, health_points = 10, lives = 5):
        self.gold_coins = gold_coins
        self.health_points = health_points
        self.lives = lives

    def __str__(self):
        return (f"Your Score is\nGold treasure = {self.gold_coins}\nHealth = {self.health_points}\nLife = {self.lives}")

    def level_up(self):
        self.lives += 1

    def collect_treasure(self):
        self.gold_coins += 1
        if self.gold_coins % 10 == 0:
            self.level_up()
        
        
    def do_battle(self, damage):
        self.health_points -= damage
        if self.health_points < 1:
            self.lives -= 1 
            self.health_points = 10
            if self.lives == 0:
                self.restart()
    
    def restart(self):
        self.gold_coins = 0
        self.health_points = 10
        self.lives = 5
        


play = Player()
# play2 = Player(30, 2, 5)
# play3 = Player (7, 9, 3)


# print(play2.do_battle(5))

# play2.collect_treasure()
# play2.collect_treasure()
# play2.collect_treasure()
# play2.collect_treasure()
# play2.collect_treasure()
# play2.collect_treasure()
# play2.collect_treasure()
# play2.collect_treasure()
# play2.collect_treasure()
# play2.collect_treasure()
# play2.collect_treasure()
# play2.collect_treasure()
# (play.do_battle(10))
# (play.do_battle(9))
# (play.do_battle(1))
# # (play.do_battle(8))
# # (play.do_battle(5))
(play.do_battle(11))
# print(play2)
print(play)
# print(play3)


