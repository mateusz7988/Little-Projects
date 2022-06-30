import time

import pygame
import math
from pygame.locals import *

#pygame.init()



class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 200 / (AU)  # 1AU = 100 pixels
    TIMESTEP = 3600 * 24  # 1 DAY

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.sun = False
        self.distance_to_sun = 0
        self.orbit = []

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        updated_points = []
        if len(self.orbit) > 2:
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        pygame.draw.circle(win, self.color, (x, y), self.radius)
        if not self.sun:
            distance_text = FONT.render(f"{round(self.distance_to_sun / 1000, 1)}km", 1, WHITE)
            win.blit(distance_text, (x - distance_text.get_width() / 2, y - distance_text.get_height() / 2))

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))

        # F = m * a


def main1():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 15, YELLOW, 1.98892 * 10 ** 30)
    sun.sun = True

    earth = Planet(-0.9832899 * Planet.AU, 0, 7, BLUE, 5.9742 * 10 ** 24)
    earth.y_vel = 30.29 * 1000

    mars = Planet(-1.38 * Planet.AU, 0, 6, RED, 6.39 * 10 ** 23)
    mars.y_vel = 24.077 * 1000

    mercury = Planet(0.307499 * Planet.AU, 0, 3, DARK_GREY, 0.330 * 10 ** 24)
    mercury.y_vel = -47.36 * 1000

    venus = Planet(0.71843 * Planet.AU, 0, 6, WHITE, 4.8685 * 10 ** 24)
    venus.y_vel = -35.02 * 1000

    jupiter = Planet(4.95 * Planet.AU, 0, 12, JUPITER, 1.898 * 10 ** 27)
    jupiter.y_vel = -13.06 * 1000

    saturn = Planet(9.04 * Planet.AU, 0, 10, SATURN, 5.6834 * 10 ** 26)
    saturn.y_vel = -9.68 * 1000

    uranus = Planet(18.4 * Planet.AU, 0, 8, URANUS, 8.6810 * 10**25)
    uranus.y_vel = -6.80 * 1000

    neptune = Planet(-29.8 * Planet.AU, 0, 7, NEPTUNE, 1.02413 * 10**26)
    neptune.y_vel = 5.43 * 1000

    planets = [sun, earth, mercury, mars, venus]

    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))
        # pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        pygame.display.update()
    pygame.quit()

def main2():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 15, YELLOW, 1.98892 * 10 ** 30)
    sun.sun = True

    earth = Planet(-0.9832899 * Planet.AU, 0, 7, BLUE, 5.9742 * 10 ** 24)
    earth.y_vel = 30.29 * 1000

    mars = Planet(-1.38 * Planet.AU, 0, 6, RED, 6.39 * 10 ** 23)
    mars.y_vel = 24.077 * 1000

    mercury = Planet(0.307499 * Planet.AU, 0, 3, DARK_GREY, 0.330 * 10 ** 24)
    mercury.y_vel = -47.36 * 1000

    venus = Planet(0.71843 * Planet.AU, 0, 6, WHITE, 4.8685 * 10 ** 24)
    venus.y_vel = -35.02 * 1000

    jupiter = Planet(4.95 * Planet.AU, 0, 12, JUPITER, 1.898 * 10 ** 27)
    jupiter.y_vel = -13.06 * 1000

    saturn = Planet(9.04 * Planet.AU, 0, 10, SATURN, 5.6834 * 10 ** 26)
    saturn.y_vel = -9.68 * 1000

    uranus = Planet(18.4 * Planet.AU, 0, 8, URANUS, 8.6810 * 10 ** 25)
    uranus.y_vel = -6.80 * 1000

    neptune = Planet(-29.8 * Planet.AU, 0, 7, NEPTUNE, 1.02413 * 10 ** 26)
    neptune.y_vel = 5.43 * 1000

    planets = [sun, jupiter, saturn, uranus, neptune]
    #, earth, mars, mercury, venus

    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    WIDTH, HEIGHT = 1400, 1000

    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    BLUE = (100, 149, 237)
    RED = (188, 39, 50)
    DARK_GREY = (80, 78, 81)
    JUPITER = (64, 68, 54)
    SATURN = (204, 153, 102)
    URANUS = (79, 208, 231)
    NEPTUNE = (41, 144, 181)


    try:
        print("Wybierz jaki model chcesz zobaczyć: \n")
        print("1 - sun, earth, mercury, mars, venus \n")
        print("2 - sun, jupiter, saturn, uranus, neptune \n")
        system = input()
        if system == "1":
            pygame.font.init()
            FONT = pygame.font.SysFont("comicsans", 16)
            WIN = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption("Planet Simulation")
            main1()
        if system == "2":
            pygame.font.init()
            FONT = pygame.font.SysFont("comicsans", 16)
            WIN = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption("Planet Simulation")
            Planet.SCALE = 20 / Planet.AU
            main2()
    except:
        print("cos nie dziala")
