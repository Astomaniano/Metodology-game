import random
class Hero:
    def __init__(self, name, health=100, power=20):
        self.name = name
        self.health = health
        self.power = power

    def alive(self):
        return self.health > 0

    def attack(self, target):
        if self.alive():
            hit = random.randint(1, self.power)
            target.health -= hit
            print(f'{self.name} нанес {target.name} {hit} урона.')

class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero('computer')

    def start(self):
        print('Битва насмерть началась!')
        attacker = self.player
        defender = self.computer

        while self.player.alive() and self.computer.alive():
            attacker.attack(defender)
            if defender.alive():
                attacker, defender = defender, attacker
            else:
                print (f'{defender.name} пал в бою.\nБитва насмерть закончилась!')
                print(f'Приветствуем нового чемпиона - {attacker.name}!')
                break

            input('Нажмите Enter для следующего хода...')

player_name = input('Введите имя своего героя: ')
game = Game(player_name)
game.start()


