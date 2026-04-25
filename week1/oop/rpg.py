from abc import ABC, abstractmethod


class Character(ABC):

    def __init__(self, name, hp):
        self.name = name
        self.__max_hp = hp
        self.__hp = hp

    def take_damage(self, amount):
        self.__hp = max(0, self.__hp - amount)
        if self.__hp == 0:
            print(f"{self.name} has been defeated!")

    def heal(self, amount):
        self.__hp = min(self.__max_hp, self.__hp + amount)
        print(f"{self.name} healed to {self.__hp} hp.")

    def is_alive(self):
        return self.__hp > 0

    def status(self):
        print(f"{self.name} — HP: {self.__hp}/{self.__max_hp}")

    @abstractmethod
    def attack(self, target):
        pass


class Warrior(Character):

    def __init__(self, name):
        super().__init__(name, 100)
        self.__rage = 0

    def attack(self, target):
        print(f"{self.name} swings a sword at {target.name} for 25 damage!")
        target.take_damage(25)
        self.__rage += 1

    def battle_cry(self):
        print(f"{self.name} lets out a battle cry and heals 20 hp!")
        self.heal(20)
        self.__rage = 0


class Mage(Character):

    def __init__(self, name):
        super().__init__(name, 70)
        self.__mana = 100

    def attack(self, target):
        print(f"{self.name} casts a fireball at {target.name} for 40 damage!")
        target.take_damage(40)
        self.__mana -= 10

    def barrier(self):
        if self.__mana >= 20:
            print(f"{self.name} raises a magic barrier and heals 15 hp!")
            self.heal(15)
            self.__mana -= 20
        else:
            print(f"{self.name} is out of mana!")


if __name__ == "__main__":
    warrior = Warrior("Thorin")
    mage = Mage("Gandalf")

    print("=== BATTLE START ===\n")

    for round_num in range(1, 5):
        print(f"--- Round {round_num} ---")

        if warrior.is_alive():
            warrior.attack(mage)
        if mage.is_alive():
            mage.attack(warrior)

        if round_num == 2:
            warrior.battle_cry()
        if round_num == 3:
            mage.barrier()

        warrior.status()
        mage.status()
        print()

        if not warrior.is_alive() or not mage.is_alive():
            break

    print("=== BATTLE END ===")
