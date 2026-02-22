class GameCharacter:
    def __init__(self,name, health, level):
        self.name = name
        self.health = health
        self.level = level
    def speak(self):
        print(f"Hi my name is {self.name}")

class Villain(GameCharacter):
    def __init__(self, name, health, level):
        super().__init__(name, health, level)
    def speak(self):
        print(f"Hi my name is {self.name} and i will kill you")
    def kill(self, game_character):
        game_character.health = 0
        print("Bang-bang, now you're dead")

player_1 = GameCharacter("Alina", 100, 1)
player_1.speak()