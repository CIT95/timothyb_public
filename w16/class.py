class Soldier:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def attack(self):
        print(f"{self.name} attacks with their{self.weapon}!")


class Knight(Soldier):
    def __init__(self, name, weapon, shield):
        super().__init__(name, weapon)
        self.shield = shield

    def attack(self):
        print(f"Knight {self.name} slashes with their {self.weapon}!")

    def defend(self):
        print(f"Knight {self.name} defends with their {self.shield}!")


class Archer(Soldier):
    def attack(self):
        print(f"Archer {self.name} shoots with their {self.weapon}!")
