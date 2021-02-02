"""
Exercice sur l'héritage
Hugo Morin
407
"""


import random


class NPC:
    def __init__(self, profession):
        self.strength = random.randint(1, 20)
        self.agility = random.randint(1, 20)
        self.constitution = random.randint(1, 20)
        self.intelligence = random.randint(1, 20)
        self.wisdom = random.randint(1, 20)
        self.charisma = random.randint(1, 20)
        self.armor_class = random.randint(1, 12)
        self.race = ""
        self.species = ""
        self.life = random.randint(1, 20)
        self.profession = profession

    def show_statistics(self):
        print(f"Force: {self.strength}")
        print(f"Agilité: {self.agility}")
        print(f"Constitution: {self.constitution}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Sagesse: {self.wisdom}")
        print(f"Charisme: {self.charisma}")
        print(f"Classe d'armure: {self.armor_class}")
        print(f"Race: {self.race}")
        print(f"Espèce: {self.species}")
        print(f"Points de vie: {self.life}")
        print(f"Profession: {self.profession}")


class Kobold(NPC):
    def __init__(self, profession):
        super().__init__(profession)
        self.race = "Humanoïde"
        self.species = "Kobold"

    def attack(self, hero):
