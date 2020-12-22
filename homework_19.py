# 1
class Weapon:
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range
    def Hit(self, actor, target):
        if target.is_alive():
            first = actor.get_coords()
            second = target.get_coords()
            h = ((first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2) ** 0.5
            if h > self.range:
                print(f'target is too far for weapon {name}')
            else:
                print(f'enemy was hit from weapon {name}, damage is {damage}')
                target.get_damage(self.damage)
        else:
            print("the enemy is already defeated")
    def __str__(self):
        return self.name

class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp
    def move(self, delta_x, delta_y):
        self.pos_x = delta_x
        self.pos_y = delta_y
    def is_alive(self):
        return self.hp != 0
    def get_damage(self, amount):
        if self.hp - amount >= 0:
            self.hp -= amount
        else:
            self.hp = 0
    def get_coords(self):
        return self.pos_x, self.pos_y

class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon
    def hit(self, target):
        if isinstance(target, MainHero):
            self.weapon.hit(self, target)
        else:
            print('I can hit only main hero')
    def __str__(self):
        return f'enemy is in the position ({self.pos_x}, {self.pos_y}) with weapon {self.name}'

class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = []
        self.number = 0
    def hit(self, target):
        if isinstance(target, BaseEnemy):
            if len(self.weapon) == 0:
                print('I am unarmed')
            elif isinstance(target, BaseEnemy):
                self.weapon.hit(self, target)
        else:
            print('I can hit only enemy')
    def add_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            self.weapon.append(weapon)
            print(f"picked up {weapon}")
        else:
            print("It's not a Weapon")
    def next_weapon(self):
        if len(self.weapon) == 0:
            print('I am unarmed')
        elif len(self.weapon) == 1:
            print('I have one weapon')
        else:
            self.weapon.append(self.weapon.pop(0))
            print(f"i take weapon {self.weapon[0]}")
    def heal(self, amount):
        if self.hp + amount >= 200:
            self.hp = 200
        else:
            self.hp += amount
        print(f'now my health is {self.hp}')