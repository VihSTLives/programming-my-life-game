class Player :
    def __init__(self) :
        self.health = 100
        self.thirst = 0
        self.hunger = 0
        self.dev_skill = 1
        self.money = 0
        self.sleep = 16

        self.max_health = 100
        self.max_thirst = 100
        self.max_hunger = 100
        self.max_sleep = 16

    def charge_health(self, amount) :
        self.health += amount

        if self.health < 0 :
            self.health = 0
        if self.health > self.max_health :
            self.health = self.max_health
    
    def charge_thirst(self, amount) :
        self.thirst += amount

        if self.thirst < 0 :
            self.thirst = 0
        if self.thirst > self.max_thirst :
            self.thirst = self.max_thirst
    
    def charge_hunger(self, amount) :
        self.hunger += amount

        if self.hunger < 0 :
            self.hunger = 0
        if self.hunger > self.max_hunger :
            self.hunger = self.max_hunger

    def charge_dev_skill(self, amount) :
        self.dev_skill += amount

    def charge_money(self, amount) :
        self.money += amount

    def charge_sleep(self, amount) :
        self.sleep += amount

        if self.sleep < 0 :
            self.sleep = 0
        if self.sleep > self.max_sleep :
            self.sleep = self.max_sleep