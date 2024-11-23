import pgzrun
import random
HEIGHT = 500
WIDTH = 500


bee = Actor("bee")
flower = Actor("flower")
flower.pos = 250,230
def draw():
    screen.blit("background",(0,0))
    bee.draw()
    flower.draw()


def update():
    if keyboard.left:
        bee.x = bee.x - 2
    if keyboard.right:
        bee.x = bee.x + 2
    if keyboard.up:
        bee.y = bee.y - 2
    if keyboard.down:
        bee.y = bee.y + 2
    if bee.colliderect(flower):
        flower.x = random.randint (10,490)
        flower.y = random.randint (10,490)



pgzrun.go()