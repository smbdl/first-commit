import random
from random import randint, choice
from enum import Enum


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    BOOST = 2
    HEAL = 3
    SAVE_DAMAGE_AND_REVERT = 4
    EXPLODE = 5
    ENERGY_TRANSFER = 6
    PROTECTION = 7


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        random_hero = random.choice(heroes)
        self.__defence = random_hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health -= self.damage

    def __str__(self):
        return f'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        if self.health > 0 and boss.health > 0:
            boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            coefficient = random.randint(2, 5)
            boss.health -= self.damage * coefficient
            print(f'Warrior hits critically {self.damage * coefficient}')


class Magic(Hero):
    def __init__(self, name, health, damage, power_points):
        super().__init__(name, health, damage, SuperAbility.BOOST)
        self.__power_points = power_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            hero.damage += self.__power_points


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            for hero in heroes:
                if hero.health > 0 and self != hero:
                    hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        boss.health -= self.__blocked_damage + self.damage


class Bomber(Hero):
    def __init__(self, name, health, damage, explode_points, is_bombed=False):
        super().__init__(name, health, damage, SuperAbility.EXPLODE)
        self.__explode_points = explode_points
        self.__is_bombed = is_bombed

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            for hero in heroes:
                if hero.health == 0 and hero != self:
                    boss.health -= self.__explode_points
                    self.__is_bombed = True
                    if self.__is_bombed:
                        self.health = 0
                        print('Bomber completed his mission.')


class Hacker(Hero):
    def __init__(self, name, health, damage, transfer_points):
        super().__init__(name, health, damage, SuperAbility.ENERGY_TRANSFER)
        self.__transfer_points = transfer_points

    def apply_super_power(self, boss, heroes):
        if self.health > 0 and round_number % 2 == 0:
            for hero in heroes:
                boss.health -= self.__transfer_points
                hero.health += self.__transfer_points


class Golem(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.PROTECTION)

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            for hero in heroes:
                boss_attack_on_heroes = hero.health - boss.damage
                self.health -= boss_attack_on_heroes/5


class AntMan(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility)


round_number = 0


def print_statistics(boss, heroes):
    print(f'ROUND {round_number} -------------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
    return all_heroes_dead


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.ability != boss.defence:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    print_statistics(boss, heroes)


def start_game():
    boss = Boss('Boss', 1000, 50)
    warrior = Warrior('Warrior', 250, 10)
    doc = Medic('Medic', 220, 5, 15)
    magic = Magic('Magic', 250, 15, 2)
    berserk = Berserk('Berserk', 230, 10)
    assistant = Medic('Assistant', 270, 5, 5)
    bomber = Bomber('Bomber', 160, 10, 100)
    hacker = Hacker('Hacker', 190, 10, 10)
    golem = Golem('Golem', 300, 5)

    heroes = [warrior, doc, magic, berserk, assistant, bomber, hacker, golem]

    print_statistics(boss, heroes)
    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)


start_game()
