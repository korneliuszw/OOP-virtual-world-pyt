from game.board.square import SquareBoard
from game.organisms.animals.antelope import Antelope
from game.organisms.animals.fox import Fox
from game.organisms.animals.player import Player
from game.organisms.animals.sheep import Sheep
from game.organisms.animals.wolf import Wolf
from game.organisms.animals.turtle import Turtle
from game.organisms.plants.belladonna import Belladona
from game.organisms.plants.dandelion import Dandelion
from game.organisms.plants.grass import Grass
from game.organisms.plants.guarana import Guarana
from game.organisms.plants.sosnowsky_weed import SosnowskyWeed
from game.point import Point
from game.world import World


def createWorld(width: int, height: int) -> World:
    boardSupplier = SquareBoard(width, height)
    player = Player(Point(1, 1))
    world = World(width, height, boardSupplier, player)
    world.get_organisms().spawn(player)
    world.get_organisms().spawn(Fox(Point(5, 4)))
    world.get_organisms().spawn(Fox(Point(7, 8)))
    world.get_organisms().spawn(Fox(Point(2, 1)))
    world.get_organisms().spawn(Fox(Point(10, 5)))
    world.get_organisms().spawn(Wolf(Point(10, 2)))
    world.get_organisms().spawn(Wolf(Point(18, 12)))
    world.get_organisms().spawn(Sheep(Point(1, 1)))
    world.get_organisms().spawn(Sheep(Point(4, 3)))
    world.get_organisms().spawn(Sheep(Point(7, 5)))
    world.get_organisms().spawn(Sheep(Point(7, 2)))
    world.get_organisms().spawn(Antelope(Point(8, 9)))
    world.get_organisms().spawn(Antelope(Point(15, 3)))
    world.get_organisms().spawn(Antelope(Point(2, 3)))
    world.get_organisms().spawn(Turtle(Point(1, 5)))
    world.get_organisms().spawn(Turtle(Point(4, 10)))
    world.get_organisms().spawn(Turtle(Point(6, 10)))
    world.get_organisms().spawn(Grass(Point(1, 9)))
    world.get_organisms().spawn(Grass(Point(2, 2)))
    world.get_organisms().spawn(Grass(Point(2, 5)))
    world.get_organisms().spawn(Grass(Point(3, 5)))
    world.get_organisms().spawn(Grass(Point(4, 5)))
    world.get_organisms().spawn(Dandelion(Point(10, 15)))
    world.get_organisms().spawn(Guarana(Point(4, 13)))
    world.get_organisms().spawn(Guarana(Point(13, 2)))
    world.get_organisms().spawn(Belladona(Point(15, 15)))
    world.get_organisms().spawn(Belladona(Point(8, 1)))
    world.get_organisms().spawn(Belladona(Point(4, 8)))
    world.get_organisms().spawn(Belladona(Point(10, 5)))
    world.get_organisms().spawn(SosnowskyWeed(Point(3, 8)))
    world.get_organisms().spawn(SosnowskyWeed(Point(9, 2)))
    return world