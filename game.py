import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True

class Star(GameElement):
    IMAGE = "Star"
    SOLID = False
    def interact(self, player):
        if len(player.inventory) >= 5:
            GAME_BOARD.draw_msg("You lose! You have rescued %d cats and you are a cat hoarder :( :( You might have aquired a few enemy bugs too!"%(len(player.inventory)))
            for i in range(0, GAME_WIDTH):
                for j in range(0, GAME_HEIGHT):
                    lose = Lose()
                    GAME_BOARD.register(lose)
                    GAME_BOARD.set_el(i, j, lose)

        if len(player.inventory) < 5:
            GAME_BOARD.draw_msg("You won! You have rescued %d cats but you are not a cat hoarder! You must really love cats!"%(len(player.inventory)))
            for i in range(0, GAME_WIDTH):
                for j in range(0, GAME_HEIGHT):
                    win = Win()
                    GAME_BOARD.register(win)
                    GAME_BOARD.set_el(i, j, win)

class Cat(GameElement):
    IMAGE = "Cat"
    SOLID = False
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just rescued a cat! You have %d items!"%(len(player.inventory)))

class Win(GameElement):
    IMAGE = "Heart"
    SOLID = True

class Lose(GameElement):
    IMAGE = "Bug"
    SOLID = True

class BadGuy(GameElement):
    IMAGE = "Horns"
    direction = 1

    # def update(self, dt):
    #     next_x = self.x + self.direction
    #     if next_x < 0 or next_x >= self.board.width:
    #         self.direction *= -1
    #         next_x = self.x
    #     self.board.del_el(self.x, self.y)
    #     self.board.set_el(next_x, self.y, self)
            
            # if (next_x, next_y) == Character() (next_x, next_y):
            #     code from end game

class Character(GameElement):
    IMAGE = "Girl"

    def next_pos(self, direction):
        if direction == "up":
            return (self.x, self.y-1)
        elif direction == "down":
            return (self.x, self.y+1)
        elif direction == "left":
            return (self.x-1, self.y)
        elif direction == "right":
            return (self.x+1, self.y)
        return None

    def keyboard_handler(self, symbol, modifier):
        direction = None
        if symbol == key.UP:
            direction = "up"
        elif symbol == key.DOWN:
            direction = "down"
        elif symbol == key.LEFT:
            direction = "left"
        elif symbol == key.RIGHT:
            direction = "right"

        self.board.draw_msg("[%s] moves %s" % (self.IMAGE, direction))

        if direction:
            next_location = self.next_pos(direction)
            if next_location:
                next_x = next_location[0]
                next_y = next_location[1]  
                
                if next_x in range(GAME_WIDTH) and next_y in range(GAME_HEIGHT):
                    
                    existing_el = self.board.get_el(next_x, next_y)
                    if existing_el:
                        existing_el.interact(self)

                    if existing_el and existing_el.SOLID:
                        self.board.draw_msg("Uh oh, a rock!")
                    elif existing_el is None or not existing_el.SOLID:
                        self.board.del_el(self.x, self.y)
                        self.board.set_el(next_x, next_y, self)     
                else:
                    print "Whoops, don't run away!"
    

    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []
    

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False

######################

GAME_WIDTH = 9
GAME_HEIGHT = 9

#### Put class definitions here ####
pass
####   End class definitions    ####

def initialize():
    """Put game initialization code here"""
    
    rock_positions = [
            (0, 4),
            (1, 2),
            (1, 6),
            (2, 0),
            (2, 3),
            (2, 5),
            (3, 7),
            (3, 8),
            (4, 1),
            (4, 2),
            (5, 4),
            (6, 0),
            (6, 2),
            (6, 4),
            (8, 1), 
            (8, 4)
        ]

    rocks = []
    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    rocks[-1].SOLID = False

    for rock in rocks:
        print rock

    cat_positions = [
            (0,1),
            (0,6),
            (1,0),
            (1,7),
            (2,2),
            (2,7),
            (3,4),
            (4,3),
            (4,6),
            (4,8),
            (5,1),
            (5,2),
            (5,5),
            (6,5),
            (7,3),
            (7,8),
            (8,0),
            (8,6),
            (8,7)
        ]

    cats = []

    for pos in cat_positions:
        cat = Cat()
        GAME_BOARD.register(cat)
        GAME_BOARD.set_el(pos[0], pos[1], cat)
        cats.append(cat)

    # cats.SOLID = False

    for cat in cats:
        print cat

    cat = Cat()
    GAME_BOARD.register(cat)
    GAME_BOARD.set_el(2,2,cat)

    player = Character()
    GAME_BOARD.register(player)
    GAME_BOARD.set_el(0, 0, player)
    print player

    star = Star()
    GAME_BOARD.register(star)
    GAME_BOARD.set_el(8,8,star)

    # for i in range(0, GAME_WIDTH):
    #     for j in range(0, GAME_HEIGHT):
    #         win = Win()
    #         GAME_BOARD.register(win)
    #         GAME_BOARD.set_el(i, j, win)

    # badguy = BadGuy()
    # GAME_BOARD.register(badguy)
    # GAME_BOARD.set_el(0,5,badguy)

    GAME_BOARD.draw_msg("KITTY GAME!")
