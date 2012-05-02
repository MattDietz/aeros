import pygame
import pymunk

import aeros.common

class Actor(object):
    def __init__(self, shape, body, color):
        self.shape = shape
        self.body = body
        self.color = color
        self.max_life = 200
        self.life = 200
        self.decay = 1
    
    def _color_ratio(self):
        ratio = float(self.life) / self.max_life
        r = self.color.r * ratio
        g = self.color.g * ratio
        b = self.color.b * ratio
        return (r, g, b, 1)

class RectangleActor(Actor):
    def __init__(self, shape, body, color, rect):
        super(RectangleActor, self).__init__(shape, body, color)
        self.rect = rect

    def draw(self, screen):
        pygame.draw.rect(screen, self._color_ratio(), self.rect)

    def bounding_rect(self):
        return self.rect

class CircleActor(Actor):
    def __init__(self, shape, body, color):
        super(CircleActor, self).__init__(shape, body, color)

    def draw(self, screen):
        r = self.shape.radius
        v = self.body.position
        rot = self.body.rotation_vector
        p = int(v.x), int(aeros.common.flipy(v.y))
        p2 = pymunk.Vec2d(rot.x, -rot.y) * r * 0.9
        pygame.draw.circle(screen, self._color_ratio(), p, int(r), 0)
        pygame.draw.line(screen, pygame.color.THECOLORS["red"], p, p+p2)

    def bounding_rect(self):
        r = self.shape.radius
        v = self.body.position
        return pygame.Rect(v.x, v.y, r, r)
