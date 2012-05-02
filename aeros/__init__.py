import math
import random

import pygame
import pygame.locals
import pymunk

import aeros.context


class StopExecution(Exception): pass


def init_pygame(context):
    pygame.init()
    mode_flags = 0 #pygame.OPENGL | pygame.DOUBLEBUF
    screen = pygame.display.set_mode(
             (context.display_width, context.display_height),
             mode_flags)
    return screen


def init_pymunk():
    pymunk.init_pymunk()
    space = pymunk.Space()
    space.gravity = pymunk.Vec2d(0.0, -900)
    return space


def init(display_size):
    context = aeros.context.AerosContext(display_size)
    context.screen_ref = init_pygame(context)
    context.space_ref = init_pymunk()
    return context


def handle_events(space):
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            raise StopExecution()
        elif event.type == pygame.locals.KEYDOWN and \
                event.key == pygame.locals.K_ESCAPE:
            raise StopExecution()
        elif event.type == pygame.locals.KEYDOWN and \
                event.key == pygame.locals.K_SPACE:
            add_ball(space)
