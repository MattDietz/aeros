import math
import random

import pygame
import pygame.locals
import pymunk

from aeros import actor
import aeros.common
import aeros.shapes



DISPLAY_DIMENSIONS = (800, 800)

fill_colors = pygame.color.THECOLORS
balls = screen = None
ball_delay = 30
objects = None
screen = None


def add_ball(space):
    x = random.randint(0, DISPLAY_DIMENSIONS[0]-1)
    y = random.randint(0, DISPLAY_DIMENSIONS[1]-1)
    mass = random.randint(2, 100)
    moment = random.randint(50, 100)
    body = pymunk.Body(mass, moment)
    body.position = (random.randint(0, DISPLAY_DIMENSIONS[0]-1),
            DISPLAY_DIMENSIONS[1]-1)
    radius = random.randint(10, 20)
    shape = pymunk.Circle(body, radius, (0, 0))
    shape.friction = 0.5
    shape.elasticity = 0.6
    space.add(body, shape)
    circle_actor = actor.CircleActor(shape, body, pygame.Color(0, 255, 0, 1))
    actors.append(circle_actor)


def add_plane(space, start_x, end_x, start_y, end_y):
    body = pymunk.Body(pymunk.inf, pymunk.inf)
    p1 = (start_x, aeros.common.flipy(start_y))
    p2 = (end_x, aeros.common.flipy(end_y))
    shape = pymunk.Segment(body, p1, p2, 0.0)
    shape.friction = 1.0
    space.add_static(shape)
    rect = pygame.Rect(start_x, start_y, end_x-start_x, end_y-start_y)
    rect_actor = actor.RectangleActor(shape, body, pygame.Color(0,0,255,1),
                                      rect)
    rect_actor.decay = 0
    actors.append(rect_actor)


def main():
    """ Teh main function lolz """
    global balls, ball_delay, actors, screen

    display_size = aeros.shapes.Size(DISPLAY_DIMENSIONS[0],
                                     DISPLAY_DIMENSIONS[1])
    context = aeros.init(display_size)
    screen = context.screen
    balls = []
    actors = []
    clock = pygame.time.Clock()

    rect = pygame.Rect(20, DISPLAY_DIMENSIONS[1] - 100,
            DISPLAY_DIMENSIONS[0] - 40, 50)
    add_plane(context.space, rect.x, rect.x+rect.w, rect.y, rect.y)
    
    dt = 1.0 / 60.0
    while True:
        screen.fill(fill_colors['black'])
        aeros.handle_events(context.space)
        ball_delay -= 1
        if ball_delay == 0:
            for i in xrange(0, 4):
                add_ball(context.space)
            ball_delay = random.randint(1, 10)
        to_remove = []
        for actor in actors:
            actor.draw(screen)
            actor.life -= actor.decay
            rect = actor.bounding_rect()
            if actor.life < 0 or rect.y < 0.0 or rect.x < 0.0 or \
                    rect.x+rect.width > DISPLAY_DIMENSIONS[0]:
                to_remove.append(actor)
        for actor in to_remove:
            context.space.remove(actor.shape)
            actors.remove(actor)
        context.space.step(dt)

        pygame.display.flip()
        clock.tick(60)
        pygame.display.set_caption("fps %d" % clock.get_fps())


if __name__ == "__main__":
    try:
        main()
    except aeros.StopExecution, e:
        print "Tidying up..."
